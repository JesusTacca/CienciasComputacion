import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sub_10.jpg')
img2=cv2.imread('sub_11.jpg')
a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))

for x in range(a):
    for y in range(b):
        x1=abs(img.item(x,y,0)-img2.item(x,y,0))
        if x1 == 0:
            img.itemset((x,y,0),0)
        else:
            img.itemset((x,y,0),x1)
            
        y1=abs(img.item(x,y,1)-img2.item(x,y,1))
        if y1 == 0:
            img.itemset((x,y,1),0)
        else:
            img.itemset((x,y,1),y1)
        z1=abs(img.item(x,y,2)-img2.item(x,y,2))
        if z1 == 0:
            img.itemset((x,y,2),0)
        else:
            img.itemset((x,y,2),z1)
cv2.imshow('asd',img)

