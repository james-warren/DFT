DFT.py - JLW 2014

This is a basic Discrete Fourier Transform (DFT) program I wrote to get used to using maths functions in Python, along with file input/output, and matplotlib for graphical display.

Upon running DFT.py, you will be prompted for a sampling frequency and input file (which is a time series, tab separated - demo versions supplied).  The input filename must be typed with the .txt extension!

Matplotlib displays the input time-domain function, then the DFT is run and the frequency spectrum output is displayed.  The Nyquist frequency is shown as a red dotted line, peaks above this are artefacts (mirror image of real peaks).

The input and output spectra are also saved as images DFTinput.png and DFToutput.png. 

The output array is also saved to a text file, DFTout.txt

Notes: 
i)  This is a DFT, not a Fast Fourier Transform, and is therefore not optimal in terms of efficiency.  
ii) There is no window function implemented at this time so you will get spectral leakage.

=====

3 demo input files are provided, these were created from a summation of sine waves in excel.

Assuming 100 Hz sampling frequency in all cases.

DFTinputtext.txt
8.5, 14.5, 24 Hz
50:1:25 amplitude

DFTinputtext2.txt
49.5 Hz alone (50 is Nyquist) - significant leakage visible

DFTinputtext3.txt
1.5, 5, 25 Hz
1:6:10 amplitude