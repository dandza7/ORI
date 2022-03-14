# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:15:27 2022

@author: Acer
"""

def makeCntDict(x):
    retVal = {i:x.count(i) for i in x}
    return retVal
    
    
lista = ["a", "b", "a", "c", "c", "a", "c"]
print(makeCntDict(lista))