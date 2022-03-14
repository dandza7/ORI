# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:48:20 2022

@author: Acer
"""
def podskup(x, y):
    if(len(x) > len(y)):
        return False
    for item in x:
        if item not in y:
            return False
        
    return True
        
list1 = ["prvi", 2, "sarma", 2.20, 2.0, "penta"]
list2 = [1, "dva", 2.201, "sarma", "dane"]
list3 = [2, "prvi", "penta"]

print(podskup(list1, list2))
print(podskup(list3, list1))
print(podskup(list3, list2))