### EJERCICIO 1

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('thresh1.png', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('thresh1.png', cv2.IMREAD_GRAYSCALE)
fils,cols=img.shape
print(fils,cols)
print(img.item(35,166))
for x in range(fils):
    for y in range(cols):
        if img.item(x,y)<=194 and 175<=img.item(x,y):
            img2.itemset((x, y), 255)
        else:
            img2.itemset((x, y), 0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(1,3,1),plt.imshow(img,'gray')
plt.subplot(1,3,2),plt.imshow(img2,'gray')
plt.subplot(1,3,3).hist(img.ravel(),256,[0,256])
plt.show()

### ERJCICIO 2

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('thresh1.png', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('thresh1.png', cv2.IMREAD_GRAYSCALE)
fils,cols=img.shape
print(fils,cols)
print(img.item(35,166))
for x in range(fils):
    for y in range(cols):
        if img.item(x,y)<=173:
            img2.itemset((x, y), 255)
        else:
            img2.itemset((x, y), 0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(1,3,1),plt.imshow(img,'gray')
plt.subplot(1,3,2),plt.imshow(img2,'gray')
plt.subplot(1,3,3).hist(img.ravel(),256,[0,256])
plt.show()

## EJERCICIO 3

import cv2 
import numpy as np 
import matplotlib.pyplot as plt
camp = cv2.imread('camp.png') 
camp2 = cv2.imread('camp.png')
print(camp[50][50])
for i in range ( len(camp) ):
	for j in range ( len(camp[i]) ):
		if( (camp[i][j][2] < 240 and camp[i][j][2] > 190) and 
		(camp[i][j][1] > 160 and camp[i][j][1] < 200) and 
		(camp[i][j][0] < 180 and camp[i][j][0] > 140)):
			camp[i][j][0]=255
			camp[i][j][1]=255
			camp[i][j][2]=255
		else:
			camp[i][j][0]=0
			camp[i][j][1]=0
			camp[i][j][2]=0
cv2.imshow('campo', camp2)
cv2.imshow('campo normal', camp)

if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows()
