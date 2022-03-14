# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:26:42 2022

@author: Acer
"""
import random

def sumColumns(m):
    x = []
    for i in range(0, len(m[0])):
        sum = 0
        for j in range(0, len(m)):
            
            sum += m[j][i]
        
        x.append(sum)
        
    return x

matrix = [[random.randint(-10, 10) for i in range(0,3)] for j in range(0,5)]

print(matrix)
print(sumColumns(matrix))