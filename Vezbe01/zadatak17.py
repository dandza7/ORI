# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:38:52 2022

@author: Acer
"""
import math
import random

def euklidskoRastojanje(x, y):
    return math.dist(x, y)


x = [random.randrange(-10,10) for i in range(0,2)]
y = [random.randrange(-10,10) for i in range(0,2)]

print(x, y, euklidskoRastojanje(x, y))