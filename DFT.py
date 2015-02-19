#attempt at discrete Fourier transform

# Attempt at a discrete fourier transform (without using any dft/fft libraries etc)
# Input file is a list of tab seperated intensity values (time series)
# at a user-declared sampling rate.

# Nyquist freq is displayed on output graph, the "artefact peaks" above this
# freq are visible as a mirror image of the "true" peaks.
#
# Note, this is a DFT not an FFT and is therefore not optimal!
# There is also no window function applied so you will get spectral leakage!

# JLW 2014

import math    #math modules (normal and complex) so can use pi, sin etc
import cmath

# ask user for sampling freq
samfreq = float(input('input sampling freq /Hz \n '))

nyquist = samfreq/2

f = open('DFTout.txt', 'w')   #open output file


### import time data from external tab sep var file~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  
### XS is string array which file imports to, then cast XS to floats in XX
inpFilename = input("Enter DFT input text filename \n")
with open(inpFilename, 'r') as inp:
     XS = inp.read().split('\t')
print(type(XS))
print(XS)

XX = [float(s) for s in XS]

print((XX))    #check data has made it into XX
print(len(XX))

### plot input function (amp vs time)- time domain
import matplotlib.pyplot as plt

igraphx = list(range(len(XX)))
for i in igraphx:
     igraphx[i]=(igraphx[i]/samfreq)    #scale correctly, given sampling freq

igraphy = XX

plt.plot(igraphx,igraphy)
plt.title("Input function - Time domain")
plt.xlabel('time /s')
plt.ylabel('amplitude')
plt.savefig('DFTinput.png')   #save as a file
plt.show()     #display on screen
plt.clf()      # clear the input graph from the plot, else output graph will just add another line
               #on top of the input one

## end of input~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### set up freq domain array.

     ## deltak = 0.50 # freq domain resolution, check Nyquist etc
maxfreq = len(XX)   # is this always the setup you'd want?

k = 0     # k is index in FF array (freq domain)
n = 0     # n is index in XX array (time domain amplitude data)
FF = [0] *(maxfreq)      # set up freq domain array load array with zeros,
                         #i.e. array has "maxfreq" members.


N = len(XX)    # This is "N", the number of time data points

### DO THE DFT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Calculating DFT")                         
while k<maxfreq:    # scan using each freq
     #print(len(XX),'lenXX')

     #print(k, 'k')
     
     while n<N:     # across all time points, limit of n<transformLength,
                    # means runs until n=(N-1)
 
            F = (XX[n])*((cmath.exp((1j*-2*(math.pi)*n*k)/N)))

            FF[k] = FF[k] + F

            #print(n)

            n=n+1
    
     k=k+1
     n = 0      #need to reset npos to 0 or while loop wont run since
                   #npos>len(XX)

### END OF DFT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#get modulus i.e. absolute value (of power spectrum) 

FA = [abs(itm) for itm in FF]
     
### plot output
ographx = list(range(len(FF)))     ###set up x axis as frequency
for i in ographx:
     ographx[i]=(ographx[i]*samfreq/len(FF)) 

ography = FA

plt.plot(ographx,ography)

# show Nyquist freq as dotted red line, same height as biggest peak
plt.plot((nyquist, nyquist),(0,max(ography)), 'r--') 

plt.title("Output Function - Freq domain")
plt.xlabel('Freq / Hz')
plt.ylabel('Power')
plt.savefig('DFToutput.png')  # save as a file
plt.show()     # show on screen
plt.clf()      # housekeeping - close plot now we've finished with it

#write output values to DFTout.txt
f.write('sample length')
f.write(str(len(XX)))
f.write('\n') 
f.write('DFT output,')
f.write(str(FA))    #FA outputs modulus of complex output i.e. power spectrum
f.write('\n')
f.close()

    
    


