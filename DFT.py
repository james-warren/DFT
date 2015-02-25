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

out_file = open('DFTout.txt', 'w')   #open output file


### import time data from external tab sep var file~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  
### tdom_string is string array which file imports to, then cast tdom_string to
### floats in tdom_flt
inp_filename = input("Enter DFT input text filename \n")
with open(inp_filename, 'r') as inp:
     tdom_string = inp.read().split('\t')
print(type(tdom_string))
print(tdom_string)

tdom_flt = [float(s) for s in tdom_string]

print((tdom_flt))    #check data has made it into tdom_flt
print(len(tdom_flt))

### plot input function (amp vs time)- time domain
import matplotlib.pyplot as plt

tdom_graphx = list(range(len(tdom_flt)))
for i in tdom_graphx:
     tdom_graphx[i]=(tdom_graphx[i]/samfreq)    #scale correctly, given sampling freq

tdom_graphy = tdom_flt

plt.plot(tdom_graphx,tdom_graphy)
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
maxfreq = len(tdom_flt)   # is this always the setup you'd want?

k = 0     # k is index in fdom_flt array (freq domain)
n = 0     # n is index in tdom_flt array (time domain amplitude data)
fdom_flt = [0] *(maxfreq)      # set up freq domain array load array with zeros,
                         #i.e. array has "maxfreq" members.


N = len(tdom_flt)    # This is "N", the number of time data points

### DO THE DFT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Calculating DFT")                         
while k<maxfreq:    # scan using each freq
     #print(len(tdom_flt),'len tdom_flt')

     #print(k, 'k')
     
     while n<N:     # across all time points, limit of n<transformLength,
                    # means runs until n=(N-1)
 
            F = (tdom_flt[n])*((cmath.exp((1j*-2*(math.pi)*n*k)/N)))

            fdom_flt[k] = fdom_flt[k] + F

            #print(n)

            n=n+1
    
     k=k+1
     n = 0      #need to reset npos to 0 or while loop wont run since
                   #npos>len(tdom_flt)

### END OF DFT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#get modulus i.e. absolute value (of power spectrum) 

fdom_abs = [abs(itm) for itm in fdom_flt]
     
### plot output
fdom_graphx = list(range(len(fdom_flt)))     ###set up x axis as frequency
for i in fdom_graphx:
     fdom_graphx[i]=(fdom_graphx[i]*samfreq/len(fdom_flt)) 

fdom_graphy = fdom_abs

plt.plot(fdom_graphx,fdom_graphy)

# show Nyquist freq as dotted red line, same height as biggest peak
plt.plot((nyquist, nyquist),(0,max(fdom_graphy)), 'r--') 

plt.title("Output Function - Freq domain")
plt.xlabel('Freq / Hz')
plt.ylabel('Power')
plt.savefig('DFToutput.png')  # save as a file
plt.show()     # show on screen
plt.clf()      # housekeeping - close plot now we've finished with it

#write output values to DFTout.txt
out_file.write('sample length')
out_file.write(str(len(tdom_flt)))
out_file.write('\n') 
out_file.write('DFT output,')
out_file.write(str(fdom_abs))    #fdom_abs outputs modulus of complex output i.e. power spectrum
out_file.write('\n')
out_file.close()

    
    


