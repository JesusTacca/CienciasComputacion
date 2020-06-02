#EJERCICIO1

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('add_1.jpg')
img2=cv2.imread('add_2.jpg')

#tamaño
a=len(img)
b=len(img[0])
c=len(img2)
d=len(img2[0])

a=max(a,c)
b=max(b,d)

img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))


for x in range(a):
    for y in range(b):
        img[x][y][0]=int((img[x][y][0]/2+img2[x][y][0]/2))
        img[x][y][1]=int((img[x][y][1]/2+img2[x][y][1]/2))
        img[x][y][2]=int((img[x][y][2]/2+img2[x][y][2]/2))

cv2.imwrite('add_3.jpg',img)


#EJERCICIO2

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('add_10.jpg')
img2=cv2.imread('add_11.jpg')

#tamaño
a=len(img)
b=len(img[0])
c=len(img2)
d=len(img2[0])

a=max(a,c)
b=max(b,d)

img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))


for x in range(a):
    for y in range(b):
        img[x][y][0]=int((img[x][y][0]/2+img2[x][y][0]/2))
        img[x][y][1]=int((img[x][y][1]/2+img2[x][y][1]/2))
        img[x][y][2]=int((img[x][y][2]/2+img2[x][y][2]/2))

cv2.imwrite('add_12.jpg',img)



