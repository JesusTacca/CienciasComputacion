##### Ejercicio1
import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

img=cv2.imread('hist5.jpg')
img2=cv2.imread('hist5.jpg', cv2.IMREAD_GRAYSCALE)

fils,cols=img2.shape
lista=[0]*256
cont=fils*cols
for x in range(fils):
    for y in range(cols):
        lista[img2.item(x,y)]=lista[img2.item(x,y)]+1

L=256
pp=[0]*256
for i in range (256):
    pp[i]=lista[i]/cont
nueva=[0]*256
print(sum(pp))
for i in range (256):
    suma=0
    for j in range(i+1):
        suma=suma+pp[j]
    suma=math.floor(suma*(L-1))
    nueva[i]=suma
    
for x in range(fils):
    for y in range(cols):
        img2.itemset((x,y),nueva[img2.item(x,y)])

hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(img,'gray')
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(img2,'gray')
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
plt.show()

##### Ejercicio 2

import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

img=cv2.imread('hist10_1.jpg', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('hist10_1.jpg', cv2.IMREAD_GRAYSCALE)

fils,cols=img.shape
lista=[0]*256
cont=fils*cols
a=250
b=350
c=180
d=250

for x in range(a,b):
    for y in range(c,d):
        lista[img.item(x,y)]=lista[img.item(x,y)]+1


L=256
pp=[0]*256
for i in range (256):
    pp[i]=lista[i]/cont
nueva=[0]*256
print(sum(pp))
for i in range (256):
    suma=0
    for j in range(i+1):
        suma=suma+pp[j]
    suma=math.floor(suma*(L-1))
    nueva[i]=suma
    
for x in range(fils):
    for y in range(cols):
        img2.itemset((x,y),nueva[img.item(x,y)])

hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(img,'gray')
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
crop_img = img[a:b, c:d]
plt.subplot(2,2,3),plt.imshow(img2,'gray')
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
cv2.imwrite('prueba.jpg',crop_img)
plt.show()

### Ejercicio 2 subimagen

import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

img=cv2.imread('hist10_1.jpg', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('hist10_1.jpg', cv2.IMREAD_GRAYSCALE)

fils,cols=img.shape
lista=[0]*256
cont=fils*cols
a=171
b=260
c=273
d=384
croppedImage = img[c:d, a:b]
img3= cv2.resize(croppedImage, (cols, fils))
#cv2.imwrite('prueba4.jpg',img3)
for x in range(fils):
    for y in range(cols):
        lista[img3.item(x,y)]=lista[img3.item(x,y)]+1


L=256
pp=[0]*256
for i in range (256):
    pp[i]=lista[i]/cont
nueva=[0]*256
print(sum(pp))
for i in range (256):
    suma=0
    for j in range(i+1):
        suma=suma+pp[j]
    suma=math.floor(suma*(L-1))
    nueva[i]=suma
    
for x in range(fils):
    for y in range(cols):
        img2.itemset((x,y),nueva[img.item(x,y)])

hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(img3,'gray')
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(img2,'gray')
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
#cv2.imwrite('prueba3.jpg',img2)
plt.show()

