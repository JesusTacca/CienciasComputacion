#######Ejercicio 1

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('contr1_1.jpg', cv2.COLOR_BGR2GRAY)
img2=cv2.imread('contr1_1.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

a=0
b=255
c=255
d=0
fils,cols=img2.shape
for x in range(fils):
    for y in range(cols):
        if c>img2.item(x,y):
            c=img2.item(x,y)
        if d<img2.item(x,y):
            d=img2.item(x,y)
print(c,d)
for x in range(fils):
    for y in range(cols):
        t=(img2.item(x,y)-c)*((b-a)/(d-c))+a
        img2.itemset((x, y), t)

plt.subplot(2,2,1),plt.imshow(img,'gray')
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(img2,'gray')
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
plt.show()

#######Ejercicio 2

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('contr3_1.jpg', cv2.COLOR_BGR2GRAY)
img2=cv2.imread('contr3_1.jpg', cv2.IMREAD_GRAYSCALE)

a=0
b=255
c=255
d=0
fils,cols=img2.shape
for x in range(fils):
    for y in range(cols):
        if c>img2.item(x,y):
            c=img2.item(x,y)
        if d<img2.item(x,y):
            d=img2.item(x,y)
print(c,d)
for x in range(fils):
    for y in range(cols):
        t=(img2.item(x,y)-c)*((b-a)/(d-c))+a
        img2.itemset((x, y), t)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(img,'gray')
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(img2,'gray')
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
plt.show()

#######Ejercicio 3

import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

img=cv2.imread('contr3_1.jpg', cv2.COLOR_BGR2GRAY)
img2=cv2.imread('contr3_1.jpg', cv2.IMREAD_GRAYSCALE)

a=0
b=255
fils,cols=img2.shape

lista=[0]*256
cont=fils*cols

for x in range(fils):
    for y in range(cols):
        lista[img2.item(x,y)]=lista[img2.item(x,y)]+1

lista2=[]
for i in range(len(lista)):
    lista2=lista2+[i]*lista[i]
print(len(lista2),cont)
x=10*cont/100
y=90*cont/100
print(x,y)
c=lista2[round(x)]
d=lista2[round(y)]
print(c,d)
for x in range(fils):
    for y in range(cols):
        t=(img2.item(x,y)-c)*((b-a)/(d-c))+a
        if t<0:
            t=0
        if t>255:
            t=255
        img2.itemset((x, y), t)
hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(img,'gray')
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(img2,'gray')
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
plt.show()
