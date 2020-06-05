import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('mul_4.jpg')

a=len(img)
b=len(img[0])

c=2

for x in range(a):
    for y in range(b):
        p=int(img.item(x,y,0)*c)
        if p > 255:
            p=255
        img.itemset((x,y,0),p)
        p=int(img.item(x,y,1)*c)
        if p > 255:
            p=255
        img.itemset((x,y,1),p)
        p=int(img.item(x,y,2)*c)
        if p > 255:
            p=255
        img.itemset((x,y,2),p)
cv2.imshow('mul_resp',img)
cv2.imwrite('mul_4R.jpg',img)



