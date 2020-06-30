import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

def crear_imagen(x,y):
    img2= np.zeros((y,x,3), np.uint8)
    color=np.array([0,0,0])
    for i in range(y):
        for j in range(x):
            f=np.random.randint(256, size=(1, 3))
            color=f[0]
            img2.itemset((i,j,0),color[0])
            img2.itemset((i,j,1),color[1])
            img2.itemset((i,j,2),color[2])
    return img2
img2=crear_imagen(80,60)
plt.imshow(img2)
plt.show()

cv2.imwrite('imagen_1.jpg',img2)