# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:16:02 2022

@author: Acer
"""
import random

def minAvgMax(x):
    firstTime = True
    min = 0;
    max = 0;
    avg = 0;
    for digit in x:
        if(firstTime):
            min = digit
            max = digit
            firstTime = False
        else:
            if(min > digit):
                min = digit
            if(max < digit):
                max = digit
        avg += digit
        
    return min, avg/len(x), max

sekvenca = []
for i in range(0,10):
    sekvenca.append(random.randint(0,10))
print(sekvenca)
print(minAvgMax(sekvenca))