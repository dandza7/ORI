# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import numpy as np
import random

#Pojedinacan zadatak se pokrece tako sto se klikne na zaglavlje i pritisne CTRL + ENTER

# %% Prvi


matr = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
jedn = np.eye(3, 3)


print(np.sum(matr*jedn))

# %% Drugi

matrA = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])
matrB = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])
print(matrA)
print(matrB)

# %% Treci 

matrA = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])
matrB = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])
print(matrA)
print(matrB)
print("Aritmeticke sredine:")
print("Cele matrice:")
print("A", np.round(np.mean(matrA),2))
print("B", np.round(np.mean(matrA),2))
print("Vrste:")
for i in range(3):
    print("A", i, np.round(np.mean(matrA[i]), 2))


for i in range(3):
    print("B", i, np.round(np.mean(matrB[i]), 2))

print("Kolone:")
for i in range(4):
    print("A", i, np.round(np.mean(np.transpose(matrA)[i]),2))
    

for i in range(4):
    print("B", i, np.round(np.mean(np.transpose(matrB)[i]),2))
    
# %% Cetvrti

matrA = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])
print(matrA)
med = np.median(matrA)
nizA = np.ravel(matrA)
x = nizA.size
found = 0
print("Median:", med)

for i in range(x):
    if(nizA[i] == med):
        print("Median found at index ", i)
        found = 1
        
if(found == 0):
    print("Median not found")


# %% Peti

matrB = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])

nizB = np.ravel(matrB)
nizB = np.sort(nizB)
matrB = np.reshape(nizB, (3,4))
matrBT = np.reshape(nizB, (4,3))
print(matrB)
print(np.transpose(matrBT))


# %% Sesti

matrA = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])
border = random.randint(0, 10)

x, y = matrA.shape
print(matrA)
print("Border: ", border)
for i in range(x):
    for j in range(y):
        if(matrA[i][j] < border):
            matrA[i][j] = border
            
            
print(matrA)

# %% Sedmi

matrB = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])
nizB = np.ravel(matrB)
nizA = np.argsort(nizB)
print(nizB)
print(nizA)

# %% Osmi

matrA = np.array([[random.randint(0, 10) for i in range(0, 4)] for i in range(0, 3)])
minBorder = random.randint(0, 10)
maxBorder = random.randint(0, 10)
if(minBorder > maxBorder):
    minBorder, maxBorder = maxBorder, minBorder

sum = 0
cnt = 0
for i in range(x):
    for j in range(y):
    
        if(matrA[i][j] >= minBorder and matrA[i][j] <= maxBorder):
            sum += matrA[i][j]
            cnt += 1
            
print(matrA)
print("Max:", maxBorder, "Min:", minBorder)
if(cnt != 0):
    print(sum/cnt)
else:
    print(0, "(Nema elemenata u opsegu)")











