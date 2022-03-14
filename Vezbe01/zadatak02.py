# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:27:07 2022

@author: Acer
"""
import random

x = []
for i in range(1, 20):
    x.append(random.randint(-20, 20))

retVal = 0
for num in x:
    if num%3 == 0:
        retVal += num
        
print(retVal)
