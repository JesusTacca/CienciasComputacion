import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('add_2.jpg')
img2=cv2.imread('add_1.jpg')

#tamaño
a=len(img)
b=len(img[0])
c=len(img2)
d=len(img2[0])

a=max(a,c)
b=max(b,d)

img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))


for x in range(a):
    for y in range(b):
        x1 = (img[x][y][0]-img2[x][y][0])
        if x1< 0:
            print(x1)
            img[x][y][0] = 255
        elif x1> 255:
            img[x][y][0] = 0
        else:
            img[x][y][0] = x1
        x1 = (img[x][y][1]-img2[x][y][1])
        if x1< 0:
            print(x1)
            img[x][y][1] = 255
        elif x1> 255:
            img[x][y][1] = 0
        else:
            img[x][y][1] = x1
        x1 = (img[x][y][2]-img2[x][y][2])
        if x1< 0:
            print(x1)
            img[x][y][2] = 255
        elif x1> 255:
            img[x][y][2] = 0
        else:
            img[x][y][2] = x1

cv2.imwrite('sub_3.jpg',img)
