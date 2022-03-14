# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:03:32 2022

@author: Acer
"""

str1 = input("String1: ")
str2 = input("String2: ")

length = len(str1) if len(str1) < len(str2) else len(str2)

par = True
ls1 = list(str1)
ls2 = list(str2)

for i in range(0, length):
    if par:
        temp = ls1[i]
        ls1[i] = ls2[i]
        ls2[i] = temp
        par = False
    else:
        par = True
        
str1 = "".join(ls1)
str2 = "".join(ls2)
print(str1)
print(str2)
