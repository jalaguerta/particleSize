# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import math
from math import pi
import statistics
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open('A1_Packing peanut dimensions.csv','r') as file:
    reader = csv.reader(file)
    radius_string = next(reader)
    height_string = next(reader)

radius_string.pop(0)
height_string.pop(0)

radius = list(map(int, radius_string))
height = list(map(int, height_string))

# Formulas for cylinder dimensions
def volume(r,h):
    V = pi*(r**2)*h
    return V


# Formula for diameter(V)
def volDiameter(V):
    vD = ((V*6)/pi)**(1/3)
    return vD

# Formula for diameter(SA)
def saDiameter(r,h):
    saD = (((2*pi*r*h) + (2*pi*(r**2))/pi))**(1/2) 
    return saD
        
#formula for sieve diameter
def sieveD(r):
    sieveDia = r*2
    return sieveDia

#Volume of packing peanuts
Volume=[]
for i in range(len(height)):
    V = volume(radius[i], height[i])/1000 #V is volume in cubic centimeters
    Volume.append(V)
    
#volDiameter of packing peanuts
VolDiameter=[]
for i in range(len(height)):
    vD = volDiameter(Volume[i])
    VolDiameter.append(vD)
    
#saDiameter of packing peanuts
SADiameter=[]
for i in range(len(height)):
    saD = saDiameter(radius[i],height[i])/100
    SADiameter.append(saD)

#plotting sieve diameter
sieveDiameter = []
for i in range(len(height)):
    sieveDia = sieveD(radius[i])*2/10
    sieveDiameter.append(sieveDia)
    
#arithmetic mean function
def arithmeticMean(lst):
    aMean = sum(lst)/len(lst)
    return aMean

massTotal = sum(Volume)*0.05
massFractionIndy = []
for i in range(len(height)):
    massFrac = 0.05*Volume[i]*VolDiameter[i]/massTotal
    massFractionIndy.append(massFrac)

massMeanDiameter = sum(massFractionIndy)


    
    
plt.hist(Volume, ec='black', bins=25)
plt.xlabel('Volume (cc)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.show()

plt.hist(VolDiameter, ec='black', bins=25)
plt.xlabel('Volume diameter (cm)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.show()

plt.hist(SADiameter, ec='black', bins=25)
plt.xlabel('Surface area diameter (cm)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.show()

plt.hist(sieveDiameter, ec='black', bins=25)
plt.xlabel('Sieve Diameter (cm)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.show()

print(arithmeticMean(VolDiameter))
print(massMeanDiameter)

