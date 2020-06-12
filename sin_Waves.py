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

# Time Delay
timeDelay = 0

# Frequencies
freqOne = 400
freqTwo = 300

# Amplitude
ampOne = 2
ampTwo = 2

# Sine Waves
sinOne = np.sin(2 * np.pi * time  * freqOne) * ampOne
sinTwo = np.sin(2 * np.pi * freqTwo * time) * ampTwo

# Sum of two frequencies
sinTot = sinOne + sinTwo

# Plot a sine wave using time and amplitude obtained for the sine wave
sinOnePlot, = plt.plot(time, sinOne)
sinTwoPlot, = plt.plot(time, sinTwo)
sinTotPlot, = plt.plot(time, sinTot)

# Plot Details
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude') 
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

# Legend Details
plt.legend(handles = [sinOnePlot, sinTwoPlot, sinTotPlot], 
           labels = ['%d Hz' % freqOne, '%d Hz' % freqTwo, 'Sum of Freq'])
#plt.legend(loc = 'best')


# Display the waves
plt.show()