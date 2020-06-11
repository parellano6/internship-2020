#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:03:24 2020

@author: newuser
"""

import numpy as np
import matplotlib.pyplot as plt 

# Get x values of the sine wave
time = np.arange(0, 3, 0.001);

# Time Delay
timeDelay = 0.25 

# Amplitude of the sine wave is sine of a variable like time
amplitude   = np.sin(2 * np.pi * time  * 3) * 2
ampTwo = np.sin(2 * np.pi * 3 * (time - timeDelay)) * 2

# Plot a sine wave using time and amplitude obtained for the sine wave
plt.plot(time, amplitude)
plt.plot(time, ampTwo)

# Give a title for the sine wave plot
plt.title('Sine wave')

# Give x axis label for the sine wave plot
plt.xlabel('Time')

# Give y axis label for the sine wave plot
plt.ylabel('Amplitude') 

plt.grid(True, which='both')

plt.axhline(y=0, color='k')

# Display the sine wave
plt.show()