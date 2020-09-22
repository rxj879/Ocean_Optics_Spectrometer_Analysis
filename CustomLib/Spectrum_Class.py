# -*- coding: utf-8 -*-
"""
   Copyright 2020 DR ROBIN RAFFE PRYCE JONES
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import glob, os
# Import library for reading, writing and removing files
 
import numpy as np
# Import the mathematical libraries

from CustomLib.Spectrum_Funcs import (Get_Dir, 
                                      Find_Line, 
                                      Create_Directory, 
                                      path_leaf,
                                      gaussian_Fitting,
                                      Extract_Column,
                                      ComputeFWHM,
                                      zerolistmaker,
                                      Generate_Two_Column_Data,
                                      Gauss)
#Import custom functions required

from CustomLib.Spectrum_PickleJar import PickleJar
# Import the class for setting up preferences files

class DataClass_Spectra:
    """Class for multiple spectra to sort lumerical data"""
    
    def __init__(self):
        """Initialise require attributes"""
        self.Data = []
        self.FileName = []
        self.Directory = Get_Dir();
        self.NumOfFiles = int
        self.Fit_Params = []

    def Import_Data(self):
        """Lumerical Data"""
        os.chdir(self.Directory)
        self.NumOfFiles = np.size(glob.glob("*.txt"))

        for file in glob.glob("*.txt"):
            File_Path = self.Directory + "/" +file
            DIR , File_Name = path_leaf(File_Path)
            self.FileName.append(File_Name)
            Line_StartNumList = Find_Line(File_Path , 'Begin Spectral Data');
            Rows_to_Skip = Line_StartNumList[0] + 1
            Data=np.genfromtxt(file, delimiter = '\t', skip_header = Rows_to_Skip); 
            self.Data.append(Data)

    def Run_Gaussian_Analysis(self):
        """Fit Gaussians to all spectra"""
        for i in range(self.NumOfFiles):
            self.Fit_Params.append(gaussian_Fitting(self.Data[i][:,0],self.Data[i][:,1]))
        sigma_array = Extract_Column(self.Fit_Params, self.NumOfFiles, 2)
        
        self.Mean_sigma = np.mean(np.absolute(sigma_array))
        
        self.Peak_Lambda = Extract_Column(self.Fit_Params, self.NumOfFiles, 1)
        self.FWHM = ComputeFWHM(sigma_array)
        self.Base_Intensity = Extract_Column(self.Fit_Params, self.NumOfFiles, 3)
        self.Gauss_Amplitude = Extract_Column(self.Fit_Params, self.NumOfFiles, 0)
        
        self.Mean_Base_Intensity = np.mean(self.Base_Intensity)
        self.Mean_Gauss_Amplitude = np.mean(self.Gauss_Amplitude)

        self.Mean_Peak_Lambda = np.mean(self.Peak_Lambda)
        self.Mean_FWHM = np.mean(self.FWHM)
        
        self.STDEV_Peak_Lambda = np.std(self.Peak_Lambda)
        self.STDEV_FWHM = np.std(self.FWHM)
        

    # Export fit params to text files in one folder
    # Compute an average spectra
    # export average spectra
    def ComputeAverageCurve(self):
        Sum_Array = zerolistmaker(len(self.Data[0][:,1]))
        for i in range(self.NumOfFiles):
            Sum_Array = Sum_Array + self.Data[i][:,1]
        
        Average_Spectrum_Intensity = Sum_Array/self.NumOfFiles
        
        self.Average_Spectrum_Data = Generate_Two_Column_Data(self.Data[i][:,0], Average_Spectrum_Intensity)


    def Generate_Average_Gaussian_Curve(self):
        Gauss_Wavelength_Points = np.linspace(min(self.Data[0][:,0]), 
                                              max(self.Data[0][:,0]),
                                              num=len(self.Data[0][:,0])*3)
        self.Average_Gaussian_Fit = []
        for i in range(len(Gauss_Wavelength_Points)):
            self.Average_Gaussian_Fit.append(Gauss(Gauss_Wavelength_Points[i],
                                                   self.Mean_Gauss_Amplitude,
                                                   self.Mean_Peak_Lambda,
                                                   self.Mean_sigma,
                                                   self.Mean_Base_Intensity))
        
        self.Average_Gaussian_Data = Generate_Two_Column_Data(Gauss_Wavelength_Points, self.Average_Gaussian_Fit)
        
        
        
    def Write_Gaussian_Statistics_Summary(self):
        """Write the Gaussian statistics to a text file"""
        Gauss_Statistics_File_Path = self.Directory + "/" + "GaussianStatistics"
        Create_Directory(Gauss_Statistics_File_Path)
        
        Data = ['Mean peak wavelength (nm): ' + str(self.Mean_Peak_Lambda) +'\n',
                'Mean FWHM (nm): ' + str(self.Mean_FWHM) +'\n',
                'STDEV peak wavelength (nm): ' + str(self.STDEV_Peak_Lambda) +'\n',
                'STDEV FWHM (nm): ' + str(self.STDEV_FWHM) +'\n']
        
        Gauss_Statistics_File_i = Gauss_Statistics_File_Path + "/"  + 'Gaussian_Statistics.txt'

        f = open(Gauss_Statistics_File_i, "w")
        for i in range(len(Data[:])):
            f.write(Data[i])
        f.close()


    def Write_Average_Files(self):
        """Write the data to new files for the importing into the Spectra Plot program"""
        Average_File_Path = self.Directory + "/" + "Average"
        Create_Directory(Average_File_Path)
        PickleJar(Average_File_Path)

        HEAD = '#Wave\t\t#Intensity'

        Average_File_i = Average_File_Path + "/"  + 'Average.txt'
        np.savetxt(Average_File_i, self.Average_Spectrum_Data,  fmt='%10.6f',
                       delimiter='\t', newline='\n', comments='',
                       header=HEAD, encoding=None)
        
        AverageGauss_File_i = Average_File_Path + "/"  + 'Average_Gaussian.txt'
        np.savetxt(AverageGauss_File_i, self.Average_Gaussian_Data,  fmt='%10.6f',
                       delimiter='\t', newline='\n', comments='',
                       header=HEAD, encoding=None)
