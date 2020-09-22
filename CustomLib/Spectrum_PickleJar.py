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

import pickle

class PickleJar:
    """Class for creating preferences for this data, I can't gaurantee that these will be
    the correct plot settings for your data when you export it from lumerical. Check that 
    the axis labels etc are what you expect"""
    
    def __init__(self, Directory):
        """initialise with attributes of plot preferences"""

#########################
        """Here are the general plot style options to add to the GUI"""

        
        self.OverrideXAxisOption = False
        self.OverrideYAxisOption = False
        self.X_Axis_LowLim = float
        self.X_Axis_HiLim = float
        self.Y_Axis_LowLim = float
        self.Y_Axis_HiLim = float
        self.X_Axis_LowLim_Override = float
        self.X_Axis_LowLim_Override = float
        self.Y_Axis_LowLim_Override = float
        self.Y_Axis_LowLim_Override = float
        self.Num_X_Ticks = 5
        self.Num_X_MinorTicks = 4
        self.Num_Y_Ticks = 5
        self.Num_Y_MinorTicks = 4
        self.Inset_XAxis_MinorNumInc =  4
        self.Inset_YAxis_NumInc = 4
        self.FigWidth = 2.5
        self.FigHeight = 1.8
        self.Legend_X_MOVE = 0.0
        self.Legend_Y_MOVE = 0.0
        self.BoxPlotOption = False
        self.LegendFrameOption = False
        self.ShowLegendOption = True
        self.YAxisTickLabelsOption = True
        self.YAxisExponentialOption = False
        self.YAxisTicksOption = False
        self.MajorXgridlinesOption = False
        self.MinorXgridlinesOption = False
        self.MajorYgridlinesOption = False
        self.MinorYgridlinesOption = False
        self.PlotTextSize = 10
        self.LabelsFontSize = 8
        self.Plotlinewidth = 0.5
        self.MinorGridlinewidth = 0.3
        self.MajorGridlinewidth = 0.4

        self.MajorGridColour = 'Grey'
        self.MinorGridColour = 'Light Grey'
        
        self.Y_AxisTitle = 'Intensity (arb. units)'
        self.X_AxisTitle = 'Wavelength (nm)'
        self.Legend_loc= 'upper left' 
        self.Y_axis_Label_Pad = 5.0
        self.X_axis_Label_Pad = 5.0
        self.Y_axis_Title_Pad = 5.0
        self.X_axis_Title_Pad = 5.0
        
        self.Norm_RadioBoxOption = 0
        self.Plot_RadioBoxOption = 0
        """"MultiPlot Options"""
        self.MultiPlot_shareyOption = False
        self.MultiPlot_sharexOption = True

#########################
        """Here are the inset plot style options to add to the GUI"""
        self.InsetPlotOption = False
        self.InsetLabelBackgroundWhite = True
        self.YInsetAxisTicksOption = False
        self.InsetLabelsTextSize = 10
        self.X_insetaxis_Label_Pad = 0.0      
        self.RShift_inset_Max = 4000
        self.RShift_inset_Min = 0
        self.Inset_XAxis_NumInc = 5
        self.Inset_LowerLeftX = 0.5
        self.Inset_LowerLeftY = 0.5
        self.Inset_Width = 0.5
        self.Inset_Height = 0.5
        self.InsetSizeIncrement = 0.01
        self.InsetLineColour = 'k'
        self.InsetLineJoin = [2,4]

################################################################
        """Redundant inset plot options"""
        self.YInsetAxisTickLabelsOption = True
        self.YInsetAxisExponentialOption = True
        self.Y_insetaxis_Label_Pad = 0.0
        
        self.save_General_prefs(Directory)
        
    def save_General_prefs(self, Directory):
        """Save general plot preferences"""
        print("Saving general preferences...")
        File = Directory+"\General_prefs.pickle"
        pickle.dump([self.Plotlinewidth,
                     self.MinorGridlinewidth,
                     self.MajorGridlinewidth,
                     self.Norm_RadioBoxOption,
                     self.Plot_RadioBoxOption,
                     self.OverrideXAxisOption,
                     self.OverrideYAxisOption,
                     self.X_Axis_LowLim,
                     self.X_Axis_HiLim,
                     self.Y_Axis_LowLim,
                     self.Y_Axis_HiLim,
                     self.X_Axis_LowLim_Override,
                     self.X_Axis_LowLim_Override,
                     self.Y_Axis_LowLim_Override,
                     self.Num_X_Ticks,
                     self.Num_X_MinorTicks,
                     self.Num_Y_Ticks,
                     self.Num_Y_MinorTicks,
                     self.Inset_XAxis_MinorNumInc,
                     self.Inset_YAxis_NumInc,
                     self.FigWidth,
                     self.FigHeight,
                     self.Legend_X_MOVE, 
                     self.Legend_Y_MOVE,
                     self.BoxPlotOption, 
                     self.LegendFrameOption, 
                     self.ShowLegendOption, 
                     self.YAxisTickLabelsOption,  
                     self.YAxisExponentialOption,
                     self.YAxisTicksOption,
                     self.MajorXgridlinesOption,
                     self.MinorXgridlinesOption,
                     self.MajorYgridlinesOption,
                     self.MinorYgridlinesOption,
                     self.MajorGridColour,
                     self.MinorGridColour,
                     self.PlotTextSize,
                     self.LabelsFontSize,
                     self.Y_AxisTitle,
                     self.X_AxisTitle,
                     self.Legend_loc,
                     self.Y_axis_Label_Pad,
                     self.X_axis_Label_Pad,
                     self.Y_axis_Title_Pad,
                     self.X_axis_Title_Pad,
                     self.MultiPlot_shareyOption,
                     self.MultiPlot_sharexOption,
                     self.InsetPlotOption,
                     self.InsetLabelBackgroundWhite,
                     self.YInsetAxisTicksOption,
                     self.InsetLabelsTextSize,
                     self.X_insetaxis_Label_Pad, 
                     self.RShift_inset_Max,
                     self.RShift_inset_Min,    
                     self.Inset_XAxis_NumInc,
                     self.Inset_LowerLeftX,
                     self.Inset_LowerLeftY, 
                     self.Inset_Width ,
                     self.Inset_Height ,
                     self.InsetSizeIncrement,
                     self.InsetLineColour,
                     self.InsetLineJoin ,
                     self.YInsetAxisTickLabelsOption ,
                     self.YInsetAxisExponentialOption,
                     self.Y_insetaxis_Label_Pad ], open(File, "wb"))
