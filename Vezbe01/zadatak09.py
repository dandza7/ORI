# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:32:50 2022

@author: Acer
"""

import random

def geoMean(x):
    retVal = 1
    for num in x:
        retVal *= num
        
    retVal = retVal**(1/len(x))
    
    return retVal

x = []
for i in range(0,5):
    x.append(random.randint(0,10))

print(x)
print(geoMean(x))