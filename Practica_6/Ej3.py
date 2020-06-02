import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sub_2.jpg')
img2=cv2.imread('sub_1.jpg')
a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))

for x in range(a):
    for y in range(b):
        p=abs(img.item(x,y,0)-img2.item(x,y,0)-100)
        img.itemset((x,y,0),p)
        p=abs(img.item(x,y,1)-img2.item(x,y,1)-100)
        img.itemset((x,y,1),p)
        p=abs(img.item(x,y,2)-img2.item(x,y,2)-100)
        img.itemset((x,y,2),p)

for x in range(0,a):
    for y in range(0,b):
        if (img.item(x,y,0)+img.item(x,y,1)+img.item(x,y,2))/3<=80 and 0<=(img.item(x,y,0)+img.item(x,y,1)+img.item(x,y,2)):
             img.itemset((x,y,0),0)
             img.itemset((x,y,1),0)
             img.itemset((x,y,2),0)
        else:
             img.itemset((x,y,0),255)
             img.itemset((x,y,1),255)
             img.itemset((x,y,2),255)
cv2.imshow('asd',img)
