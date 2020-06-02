import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('add_10.jpg')
img2=cv2.imread('add_11.jpg')
a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))


for x in range(a):
    for y in range(b):
        p=int(img.item(x,y,0)/2+img2.item(x,y,0)/2)
        img.itemset((x,y,0),p)
        p=int(img.item(x,y,1)/2+img2.item(x,y,1)/2)
        img.itemset((x,y,1),p)
        p=int(img.item(x,y,2)/2+img2.item(x,y,2)/2)
        img.itemset((x,y,2),p)
cv2.imshow('asd',img)



