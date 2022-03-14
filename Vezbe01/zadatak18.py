# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:43:20 2022

@author: Acer
"""
import random

def makeMatrix(x, y):
    return [[random.randint(-10, 10) for i in range(0,x)] for j in range(0,y)]  


matrix = makeMatrix(int(input("Broj kolona matrice:")), int(input("Broj vrsta matrice:")))
for i in range(0, len(matrix)):
    print(matrix[i])