# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:41:30 2022

@author: Acer
"""

def spoj(x, y):
    retVal = []
    for item in x:
        if item not in retVal:
            retVal.append(item)
    for item in y:
        if item not in retVal:
            retVal.append(item)
            
    return retVal


list1 = ["prvi", 2, "sarma", 2.20, 2.0, "penta"]
list2 = [1, "dva", 2.201, "sarma", "dane"]

print(spoj(list1, list2))