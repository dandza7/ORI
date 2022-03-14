# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:24:27 2022

@author: Acer
"""

import random


def makeDic(x):
    dic = {
        "decimal" : x,
        "binary" : bin(x)[2:],
        "hexadecimal" : hex(x)
    }
    return dic
x = random.randint(0,100)

print(makeDic(x))
