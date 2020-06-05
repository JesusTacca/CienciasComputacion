import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sub_1.jpg')
img2=cv2.imread('sub_2.jpg')
a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))

nMax = 255
nMin = 0

Max = 0
Min = 255
for x in range(a):
    for y in range(b):
        p=(img.item(x,y,0)/img2.item(x,y,0))
        img.itemset((x,y,0),p*100)
        if p <= Min:
            Min = p
        if p >= Max:
            Max = p
        p=(img.item(x,y,1)/img2.item(x,y,1))
        img.itemset((x,y,1),p*100)
        if p <= Min:
            Min = p
        if p >= Max:
            Max = p
        p=(img.item(x,y,2)/img2.item(x,y,2))
        img.itemset((x,y,2),p*100)
        if p <= Min:
            Min = p
        if p >= Max:
            Max = p
            
Min=Min*100
Max=Max*100
print(Min)
print(Max)
cv2.imwrite('texto_dividido.jpg',img)
print(int((((img.item(x,y,0)-(Min))*((nMax-nMin)/(Max-Min)))+nMin)))

for x in range(a):
    for y in range(b):
        
        p=int((((img.item(x,y,0)-(Min))*((nMax-nMin)/(Max-Min)))+nMin))
        if p >= 255:
            p=255
        if p <= 0:
            p=0
        img.itemset((x,y,0),p)
        p=int((((img.item(x,y,1)-(Min))*((nMax-nMin)/(Max-Min)))+nMin))
        if p >= 255:
            p=255
        if p <= 0:
            p=0
        img.itemset((x,y,1),p)
        p=int((((img.item(x,y,2)-(Min))*((nMax-nMin)/(Max-Min)))+nMin))
        if p >= 255:
            p=255
        if p <= 0:
            p=0
        img.itemset((x,y,2),p)

for x in range(0,a):
    for y in range(0,b):
        if (img.item(x,y,0)+img.item(x,y,1)+img.item(x,y,2))/3<=170 and 0<=(img.item(x,y,0)+img.item(x,y,1)+img.item(x,y,2)):
             img.itemset((x,y,0),0)
             img.itemset((x,y,1),0)
             img.itemset((x,y,2),0)
        else:
             img.itemset((x,y,0),255)
             img.itemset((x,y,1),255)
             img.itemset((x,y,2),255)

cv2.imshow('asd',img)
cv2.imwrite('texto_bueno.jpg',img)

