# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:52:01 2022

@author: Acer
"""

x = int(input("Broj:"))
string = str(x)
cnt = len(string)-1
retVal = 0
for digit in string:
    retVal += int(digit) * 10**cnt if int(digit)%2==0 else 0
    cnt -= 1
    
print(retVal)