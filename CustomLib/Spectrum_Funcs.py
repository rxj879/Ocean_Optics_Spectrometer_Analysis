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
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

from tkinter import filedialog
from tkinter import Tk
# Import ask save / open file and directory dialogue box library

import os
# Import os library for removing files

import re
# import the regular expression operations library for the scientific notation

import ntpath
# import the library for handling windows paths

def path_leaf(path):
    """ Function for splitting the file path"""
    head, tail = ntpath.split(path)
    return head, tail.split(".")[0] 

def Create_Directory(dirName):
    """Check and create a directory"""
    try:
        # Create target Directory
        os.mkdir(dirName)
        
    except FileExistsError:
        pass     
    
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    else:    
        pass
    
def Get_Dir (Idir = None):
    "This uses tkinter to ask for the directory where the data is in text files"
    root = Tk();
    root.directory =  filedialog.askdirectory(initialdir = Idir, title = "Select directory/folder with the text data. Then hit import!");
    root.withdraw();
    return root.directory;

def Find_Line(File , Text_Search):
    """Function to find the line number where a string appears in the file """
    with open(File,'r') as f:
        content = f.readlines()

    index = [x for x in range(len(content)) if Text_Search in content[x]]
    f.close()
    return index

def Read_Line(File, Line_Num):
    with open(File, 'r') as f:
        content = f.readlines()
    return content[Line_Num]

def Determine_ScaleFactor(String):
    if 'lambda(m)' in String:
        ScaleFactor = 1E9
    elif 'lambda(microns)' in String:
        ScaleFactor = 1E3
    return ScaleFactor
        
def Extract_NumberData(string):
    """ Function to import data in scientific notation """
    scinot = re.compile('[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)')
    List = [float(s) for s in re.findall(scinot, string)]
    return List

def gaussian_Fitting(x, y):
    mean = sum(x * y) / sum(y)
    sigma = np.sqrt(sum(y * (x - mean)**2) / sum(y))
    base = min(y)
    popt,pcov = curve_fit(Gauss, x, y, p0=[max(y), mean, sigma, base])
    
    return popt
    
def Gauss(x, a, x0, sigma, base):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2)) +base

def Extract_Column(arrays, NumofArrays, column):
    sigma = []
    for i in range(NumofArrays):
        sigma.append(arrays[i][column])
    return sigma

def ComputeFWHM(sigma):
    FWHM = []
    for i in range(len(sigma)):
        FWHM.append(abs(sigma[i])*2*np.sqrt(2*np.log(2)))
    return FWHM

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def Generate_Two_Column_Data(Column1, Column2):
    Data = []
    for i in range(len(Column1)):
        Data.append([Column1[i], Column2[i]])
    return Data
    
    
    