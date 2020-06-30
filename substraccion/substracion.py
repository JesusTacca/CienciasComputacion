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

#---------------------------------------------------
img=cv2.imread('paper7.jpg')
img2=cv2.imread('paper6.jpg')
a1=max(len(img),len(img2))
b1=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b1,a1))
img2=cv2.resize(img2,(b1,a1))
print(a1,b1)
c=2
w_s=11


for x in range(a1):
    for y in range(b1):
        p=abs(img.item(x,y,0)-img2.item(x,y,0)-40)
        img.itemset((x,y,0),p)
        p=abs(img.item(x,y,1)-img2.item(x,y,1)-40)
        img.itemset((x,y,1),p)
        p=abs(img.item(x,y,2)-img2.item(x,y,2)-40)
        img.itemset((x,y,2),p)

ac=0
bc=255
lista=[0]*256
cont=a1*b1
for x in range(a1):
    for y in range(b1):
        lista[img2.item(x,y,0)]=lista[img2.item(x,y,0)]+1
        lista[img2.item(x,y,1)]=lista[img2.item(x,y,1)]+1
        lista[img2.item(x,y,2)]=lista[img2.item(x,y,1)]+1
lista2=[]
for i in range(len(lista)):
    lista2=lista2+[i]*lista[i]
xc=5*cont/100
yc=95*cont/100
cc=lista2[round(xc)]
dc=lista2[round(yc)]

for x in range(a1):
    for y in range(b1):
        t=(img.item(x,y,0)-cc)*((bc-ac)/(dc-cc))+ac
        if t<0:
            t=0
        if t>255:
            t=255
        img2.itemset((x, y,0), t)
        t=(img.item(x,y,1)-cc)*((bc-ac)/(dc-cc))+ac
        if t<0:
            t=0
        if t>255:
            t=255
        img2.itemset((x, y,1), t)
        t=(img.item(x,y,2)-cc)*((bc-ac)/(dc-cc))+ac
        if t<0:
            t=0
        if t>255:
            t=255
        img2.itemset((x, y,2), t)
img=img2

"""
for x in range(a1):
    for y in range(b1):
        lista[0][img2.item(x,y,0)]=lista[0][img2.item(x,y,0)]+1
        lista[1][img2.item(x,y,1)]=lista[1][img2.item(x,y,1)]+1
        lista[2][img2.item(x,y,2)]=lista[2][img2.item(x,y,2)]+1
L=256
p=[[0]*256,[0]*256,[0]*256]
for i in range (256):
    p[0][i]=lista[0][i]/cont
    p[1][i]=lista[1][i]/cont
    p[2][i]=lista[2][i]/cont
nueva=[[0]*256,[0]*256,[0]*256]
print([sum(i) for i in p])
for i in range (256):
    suma=[0,0,0]
    for j in range(i+1):
        suma[0]=suma[0]+p[0][j]
        suma[1]=suma[1]+p[1][j]
        suma[2]=suma[2]+p[2][j]
        suma[0]=math.floor(suma[0]*(L-1))
        suma[1]=math.floor(suma[1]*(L-1))
        suma[2]=math.floor(suma[2]*(L-1))
        nueva[0][i]=suma[0]
        nueva[1][i]=suma[1]
        nueva[2][i]=suma[2]
for x in range(fils):
    for y in range(cols):
        img2.itemset((x,y,0),nueva[0][img.item(x,y,0)])
        img2.itemset((x,y,1),nueva[1][img.item(x,y,1)])
        img2.itemset((x,y,2),nueva[2][img.item(x,y,2)])
"""



"""
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
"""

#cv2.imshow('resp',img2)
cv2.imwrite('paper4.jpg',img)
