import cv2
import os
import numpy as np
import matplotlib.colors as colors
import math

croped = cv2.imread("Flammable_Solid.jpg", -1)
croped = cv2.resize(croped,(300,300))

data = []
for i in range(0, 300, 40):
    for x in range(0, 300, 40):
        data.append(croped[i, x])
data = np.asarray(data)
data = (data.astype(float)) / 255.0
data = data[..., 0].flatten()

croped1 = cv2.imread("Flammable_Gas.jpg", -1)
croped1 = cv2.resize(croped1,(300,300))

data1 = []
for i in range(0, 300, 40):
    for x in range(0, 300, 40):
        data1.append(croped1[i, x])
data1 = np.asarray(data1)
data1 = (data1.astype(float)) / 255.0
data1 = data1[..., 0].flatten()

croped2 = cv2.imread("Flammable.jpg", -1)
croped2 = cv2.resize(croped2,(300,300))

data2 = []
for i in range(0, 300, 40):
    for x in range(0, 300, 40):
        data2.append(croped2[i, x])
data2 = np.asarray(data2)
data2 = (data2.astype(float)) / 255.0
data2 = data2[..., 0].flatten()

print(np.all(data == data1))
print(np.all(data == data2))
print(np.all(data1 == data2))

