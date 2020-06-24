#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:26:12 2020

@author: newuser
"""

import numpy as np
import matplotlib.pyplot as plt

# User input for frequency
frequency = -1
while frequency <= 0:
    print ("\nPlease enter your frequency in Hz. (syntax for scientific notation is e.g. '1000 = 1e3' or '0.001 = 1e-3')")
    frequency = float(input())
    if frequency <= 0:
        print("\nValue cannot be less than or equal to zero!\n")
        
# User input for number of sensors
numSens = -1
while numSens < 1 or (numSens.is_integer() == False):
    print ("\nPlease enter a positive integer for the number of sensors wanted (enter 0 for no sensors).")
    numSens = float(input())
    if numSens <= 1:
        print("\nValue cannot be less than 1!\n")
    if numSens.is_integer() == False:
        print("\nValue has to be an integer!\n")

# User input for x and y values for originating sound    
print ("\nPlease enter the X value for the location of the sound (in meters)")
xVal = float(input())
print ("\nPlease enter the Y value for the location of the sound (in meters)")
yVal = float(input())

        


# Plot Details
fig, ax = plt.subplots()
ax.grid(True, which='both')

# Boldens X and Y axis
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# finding slope 
if yVal == 0:
    slope = 0
else:
    slope = -1 * xVal / yVal

soundSpeed = 343.4218310025016  # speed of sound in meters per second
wavelength = soundSpeed / frequency # wavelength

distSens = wavelength / 2 # distance between sensors in meters
distOri = distSens / 2 # distance microphones are from origin

print ("\nThe wavelength is %.10f meters" % wavelength)
print ("\nThe distance between the sensors is %.10f meters" % distSens)

circRad = 0.1 # radius of microphones (circles) in meters
negLoc = -1 * distOri # location of first microphone when even (negative)
posLoc = distOri # location of second microphone when even (positive)
distLast = 0 # Distance from origin to last sensor

# Space needed between first and last sensor
totDistSens = distSens * numSens

if (numSens % 2) != 0:
    distLast = int(numSens / 2) * distSens # Distance from origin to last sensor
    circle1 = plt.Circle((0, 0), circRad, color='blue')
    # Plotting Sensor
    ax.add_artist(circle1)
    for countOdd in range(int(numSens / 2)):
        sensOne = plt.Circle((-1 * distSens * (countOdd + 1), 0), circRad, color='blue')
        sensTwo = plt.Circle((distSens * (countOdd + 1), 0), circRad, color='blue')
        # Plotting Sensors
        ax.add_artist(sensOne)
        ax.add_artist(sensTwo)
else:
    distLast = ((numSens / 2) - 1) * distSens + distOri # Distance from origin to last sensor
    circle1 = plt.Circle((negLoc, 0), circRad, color='blue')
    circle2 = plt.Circle((posLoc, 0), circRad, color='blue')
    # Plotting Sensors
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    for countEven in range(int(numSens / 2)):
        distLast += 1
        sensOne = plt.Circle((((-1 * distSens) * countEven) + negLoc, 0), circRad, color='blue')
        sensTwo = plt.Circle(((distSens * countEven) + posLoc, 0), circRad, color='blue')
        # Plotting Sensors
        ax.add_artist(sensOne)
        ax.add_artist(sensTwo)
    
#for countSens in range(numSens):
#    plt.Circle((-1 * distOri, 0), circRad, color='blue')

countLim = np.linspace(yVal, 0, 10)
arrayLen = len(countLim)

for count in range(30):
    xMin = -5
    xMax = 5
    x = np.linspace(xMin, xMax,1000)
    if (xVal > 0 and yVal < 0) or (xVal < 0 and yVal < 0):
        count = count * -1
        
    if yVal == 0:
        if xVal < 0:
            locLine = plt.axvline(x = -1 * count, ymin = xMin, ymax = xMax, color = 'r')
        else:
            locLine = plt.axvline(x = count, ymin = xMin, ymax = xMax, color = 'r')
    else:
        y = slope * x + count
        locLine, = plt.plot(x, y, '-r')
    #if y[count] >= yVal and x[count] >= xVal:
        #break

# Sound location
soundLoc = plt.Circle((xVal, yVal), 0.15, color='g') # location of sound

# Plotting shapes
ax.add_artist(soundLoc)

# Formatting Axis
maxAxis = max(abs(xVal), abs(yVal)) + 1
axes = plt.gca()
axes.set_xlim([-1 * maxAxis, maxAxis])
axes.set_ylim([-1 * maxAxis, maxAxis])

# Legend
plt.legend([circle1, soundLoc, locLine], ["Sensors", "Location of Sound", "Sound Waves"])

#fig.savefig('plotcircles.png')