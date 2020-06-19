### EJERCICIO 1

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('log_3.png', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('log_3.png', cv2.IMREAD_GRAYSCALE)
fils,cols=img.shape
print(fils,cols)
print(img.item(35,166))
for x in range(fils):
    for y in range(cols):
        if img.item(x,y)<=150 and 76<=img.item(x,y):
            img2.itemset((x, y), 255)
        else:
            img2.itemset((x, y), 0)
cv2.imwrite('img1.jpg',img2)
