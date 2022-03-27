#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:57:28 2022

@author: debian
"""

# %% z1

import pandas as pd

data = pd.read_csv("/home/debian/Desktop/Aircraft_Noise_Complaint_Data(2).csv")

print(data)

print(data.dtypes)

# %% z2 

print("Broj redova: ", data.shape[0])

# %% z3

for column in data:
    for pod in data[column]:
        if pod == None:
            print("Nasao")
            
print(data.isna().sum())
data.dropna(inplace = True)

print("Broj redova: ", data.shape[0])

# %% z4
print("Broj jedinstvenih zajednica: ", data['Community'].unique().size)


# %% z5
import numpy as np

a=data.groupby('Month')
print(np.round(a["Total Complaints"].mean(), 2))
print(np.round(a["Total Complaints"].max(), 2))
print(np.round(a["Total Complaints"].min(), 2))


# %%z6

x = data["Total Complaints"]

maxi = x.idxmax()

print(data.iloc[maxi])

# %%z7

x = data[data['Community'] == 'Palo Alto']

print(x.describe())

# %%z8

a=data.groupby('Community')
print(np.round(a["Total Number of Callers"].mean(), 2))


# %%z9

x = data[data['Year'] == 2018]

print(x)

# %%z10

x.drop(columns=["Community"], inplace=True)
print(x)

# %%z11
y = data[data['Year'] == 2018]
y['Month'].replace([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                   ["J","F","M","A","M","J","J", "A", "S", "O", "N", "D"],
                   inplace=True)

print(y)
        
# %%z12
z = data[data['Year'] == 2018]
print(z.groupby(["Month", "Year"]).agg(np.sum))

# %%z11

# NE BACA WARNING ALI ISPISUJE SAMO MONTH KOLONU
w = data[data['Year'] == 2018]
print(w['Month'].replace({
                        1:"J",
                        2:"F",
                        3:"M",
                        4:"A",
                        5:"M",
                        6:"J",
                        7:"J",
                        8:"A",
                        9:"S",
                        10:"O",
                        11:"N",
                        12:"D"
                        }))

