import cv2
import random
import math
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('perro.jpg')
img2=cv2.imread('guerra.jpg')
a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))

C=0.7

for x in range(a):
    for y in range(b):
        
        x1=abs(math.floor(img.item(x,y,0)*(C))  +  math.floor(img2.item(x,y,0)*(1-C)))
        img.itemset((x,y,0),x1)
        x1=abs(math.floor(img.item(x,y,1)*(C))  +  math.floor(img2.item(x,y,1)*(1-C)))
        img.itemset((x,y,1),x1)
        x1=abs(math.floor(img.item(x,y,2)*(C))  +  math.floor(img2.item(x,y,2)*(1-C)))
        img.itemset((x,y,2),x1)
        
cv2.imshow('asd',img)
cv2.imwrite('flashbacks.jpg',img)
