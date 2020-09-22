# Ocean_Optics_Spectrometer_Analysis
Analyse ouput text files of spectra from Ocean Optics Spectrometer

These scripts take the text output from Ocean Optics import the data and fits 
Gaussians to all spectra. The Gaussian fit parameters and statistics are exported
to a text file and the time average spectra is exported to a format siutable for
the Spectra-Plot application along with a time average Gaussian.

1) In OceanView, export multiple spectra into a text format. 
2) Open the script "main.py" in your IDE such as spyder. 
3) run the program --> press select file --> then navigate dialogue window and 
	select the folder containing the exported text files
4) Review Gaussian Statistics in the "GaussianStatistics" Folder
5) Run "Spectra-Plot" App to view exported time average spectra and Gaussian fit
	in "Average" folder

