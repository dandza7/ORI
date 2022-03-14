# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:36:48 2022

@author: Acer
"""
import random

def getDif(x):
    retVal = []
    for i in range(0,len(x)-1):
        retVal.append(x[i]-x[i+1])

    return retVal

x = []
for i in range(0,10):
    x.append(random.randint(0,10))
    
print(x)
print(getDif(x))