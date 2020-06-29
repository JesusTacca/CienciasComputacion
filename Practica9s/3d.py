import cv2
import math
import random
import numpy as np
from matplotlib import pyplot as plt

def nombre(img,m):
    fils,cols,c = img.shape
    a1 = math.ceil(fils*m)
    b1 = math.ceil(cols*m)
    img2 = np.zeros((a1,b1,3),np.uint8)
    for x in range(a1):
        for y in range(b1):
            a2 = math.ceil(x/m)
            b2 = math.ceil(y/m)
            if a2 < fils and b2 < cols:
                img2.itemset((x,y,0),img.item(a2,b2,0))
                img2.itemset((x,y,1),img.item(a2,b2,1))
                img2.itemset((x,y,2),img.item(a2,b2,2))
    return img2

img=cv2.imread('thresh3.png')

img2 = nombre(img,5)

cv2.imshow('asd',img2)
