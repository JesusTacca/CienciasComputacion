import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sub_2.jpg')
img2=cv2.imread('sub_1.jpg')

#tamaño
a=len(img)
b=len(img[0])
c=len(img2)
d=len(img2[0])

a=max(a,c)
b=max(b,d)

for x in range(a):
    for y in range(b):
        
        x1=img[x][y][0]
        x2=img2[x][y][0]

        img[x][y][0] = abs(int(x1)-100-int(x2))
        y1=img[x][y][1]
        y2=img2[x][y][1]

        img[x][y][1] = abs(int(y1)-100-int(y2))
        z1=img[x][y][2]
        z2=img2[x][y][2]

        img[x][y][2] = abs(int(z1)-100-int(z2))

for x in range(0,a):
    for y in range(0,b):
        if ((int(img[x][y][0])+int(img[x][y][1])+int(img[x][y][2]))/3<=80 and 0<=(int(img[x][y][0])+int(img[x][y][1])+int(img[x][y][2]))/3 ):
             img[x][y][0] = 0
             img[x][y][1] = 0
             img[x][y][2] = 0
        else:
             img[x][y][0] = 255
             img[x][y][1] = 255
             img[x][y][2] = 255
cv2.imwrite('sub_3.jpg',img)
