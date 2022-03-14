# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:59:48 2022

@author: Acer
"""

string = input("Random String: ")
retVal = ""
for char in string:
    retVal += char
    if char.isdigit():
        retVal += char
        
print(retVal)