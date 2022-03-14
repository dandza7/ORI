# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:58:14 2022

@author: Acer
"""

def strDict(x):
    retVal = {
    }
    for key in x:
        if isinstance(x[key], str):
            retVal[key] = x[key]

    return retVal



recnik = {
    '1' : 1,
    '2' : "dva",
    '3' : "tri",
    '4' : 4,
    '5' : 5,
    '6' : "sest"
}

print(strDict(recnik))