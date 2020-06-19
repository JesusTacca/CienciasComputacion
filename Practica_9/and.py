import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

def umbral(imagen,x,y,w):
    r=int((w-1)/2)
    x = x-r
    y = y-r
    newx = 0
    newy = 0
    promR = 0
    promG = 0
    promB = 0
    divi = 0
    for i in range(w):
        for j in range(w):
            newx=x+i
            newy=y+j
            if newx>=0 and newy>=0 and newx<len(imagen) and newy<len(imagen[0]):
                promR=promR+imagen.item(newx,newy,0)
                promG=promG+imagen.item(newx,newy,1)
                promB=promB+imagen.item(newx,newy,2)
                divi=divi+1
    promR=(promR/divi)
    promG=(promG/divi)
    promB=(promB/divi)
    return promR,promG,promB


img=cv2.imread('paper6.jpg')
img2=cv2.imread('paper6.jpg')
a1=max(len(img),len(img2))
b1=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b1,a1))
img2=cv2.resize(img2,(b1,a1))
print(a1,b1)
c=2
w_s=11

for i in range(a1):
    for j in range(b1):
        r,g,b = umbral(img,i,j,w_s)
        if r-c>img.item(i,j,0):
            img2.itemset((i,j,0),0)
            img2.itemset((i,j,1),0)
            img2.itemset((i,j,2),0)
        else:
            img2.itemset((i,j,0),255)
            img2.itemset((i,j,1),255)
            img2.itemset((i,j,2),255)
        
#cv2.imshow('resp',img2)
cv2.imwrite('paper5.jpg',img2)




