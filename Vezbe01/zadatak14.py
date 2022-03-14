# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:11:15 2022

@author: Acer
"""

def filterDict(x):
    retVal = []
    for key in x:
        if x[key] not in retVal:
            retVal.append(x[key])
    return retVal


recnik = {
    1 : 1,
    2 : "jedan",
    3 : 10,
    4 : 1,
    5 : 10,
    6 : "sest",
    7 : 10,
    "jedan" : "miso",
    9 : 22,
    10 : "sest"
}

print(filterDict(recnik))