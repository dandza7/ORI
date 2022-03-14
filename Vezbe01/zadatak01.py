# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = int(input("Unesi prvi broj: "))
y = int(input("Unesi drugi broj: "))
z = int(input("Unesi treci broj: "))
print(x if y > x and z > x else y if x > y and z > y else z)
