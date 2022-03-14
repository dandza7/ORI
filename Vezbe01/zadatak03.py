# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:38:41 2022

@author: Acer
"""

str = input("Random string: ")
retVal = ""
for char in str:
    if char.isdigit() or (char >= 'A' and char <= 'F') or (char >= 'a' and char <= 'f') or char == 'x' or char == 'X':
        #print(char)
        retVal += char
    else:
        retVal += ' '

print("Filter string:",retVal)