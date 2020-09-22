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

from CustomLib.Spectrum_Class import DataClass_Spectra
# Import the custom class for sorting the spectrum

if __name__ == '__main__':
    """instantiate objects and process""" 
    Spectrum_Data = DataClass_Spectra()
    Spectrum_Data.Import_Data()

    Spectrum_Data.Run_Gaussian_Analysis()
    Spectrum_Data.Write_Gaussian_Statistics_Summary()
    Spectrum_Data.ComputeAverageCurve()
    Spectrum_Data.Generate_Average_Gaussian_Curve()
    Spectrum_Data.Write_Average_Files()