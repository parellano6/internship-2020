#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:03:24 2020

@author: newuser
"""

import numpy as np
import matplotlib.pyplot as plt 

# Get x values of the sine wave
time = np.arange(0, .01, 0.000001);

# User input for frequency
frequency = -1
while frequency <= 0:
    print ("\nPlease enter your frequency in Hz. (syntax for scientific notation is e.g. '1000 = 1e3' or '0.001 = 1e-3')")
    frequency = float(input())
    if frequency <= 0:
        print("\nValue cannot be less than or equal to zero!\n")

# Amplitude
print("\nPlease enter the amplitude.")
amp = float(input())
        
# Selection
select = -1
while select != 0 and select != 1:
    print("\nPlease enter '0' for phase shift, and '1' for time delay.")
    select = float(input())
    if select != 0 and select != 1:
        print("\nInvalid Value!\n")

# Time Delay
if select == 1:
    print ("\nPlease enter a value for time delay (enter a negative number for a delay and a positive for an advance).")
    timeShift = float(input())
    # New wave
    sinTwo = amp * np.sin(2 * np.pi * (time - timeShift) * frequency)

# Phase Shift
if select == 0:
    print("\nPlease enter a value for the phase shift (in degrees)") 
    phaseShift = float(input())
    phaseShift = phaseShift * np.pi / 180
    # New wave
    sinTwo = amp * np.sin(2 * np.pi * time * frequency + phaseShift)

# Sine Waves
sinOne = amp * np.sin(2 * np.pi * time * frequency)

# Sum of two frequencies
#sinTot = sinOne * sinTwo

# Plot a sine wave using time and amplitude obtained for the sine wave
sinOnePlot, = plt.plot(time, sinOne)
sinTwoPlot, = plt.plot(time, sinTwo)
#sinTotPlot, = plt.plot(time, sinTot)

# Plot Details
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude') 
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

# Legend Details
plt.legend(handles = [sinOnePlot, sinTwoPlot], 
           labels = ['Original Wave' % sinOne, 'Shifted Wave' % sinTwo])
#plt.legend(loc = 'best')

# Plot Details
#fig, ax = plt.subplots()

# Display the waves
plt.show()
