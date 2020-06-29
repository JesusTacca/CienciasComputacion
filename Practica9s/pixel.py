import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

#img=cv2.imread('gran-dragon-mitologia.jpg',0)

#fils=len(img)
#cols=len(img[0])

#A=np.zeros((fils,cols))

#for i in range(fils):
#    A.T[i]=int(fils**i)

def interolacion(img,x,y):
    x0 = np.floor(x).astype(int)
    x1 = x0 + 1
    y0 = np.floor(y).astype(int)
    y1 = y0 + 1

    x0 = np.clip(x0, 0, img.shape[1]-1);
    x1 = np.clip(x1, 0, img.shape[1]-1);
    y0 = np.clip(y0, 0, img.shape[0]-1);
    y1 = np.clip(y1, 0, img.shape[0]-1);

    Ia = img[ y0, x0 ]
    Ib = img[ y1, x0 ]
    Ic = img[ y0, x1 ]
    Id = img[ y1, x1 ]

    wa = (x1-x) * (y1-y)
    wb = (x1-x) * (y-y0)
    wc = (x-x0) * (y1-y)
    wd = (x-x0) * (y-y0)

    return wa*Ia + wb*Ib + wc*Ic + wd*Id

#img=cv2.imread('gran-dragon-mitologia.jpg',0)
img=cv2.imread('gran-dragon-mitologia.jpg',0)

img2= interolacion(img,4,8)

cv2.imshow('resultado',img2)

#cols,fils=img.shape

#fils=len(img)
#cols=len(img[0])



#factor=2

#for x in range(fils):
#    for y in range(cols):
#        p=float(img.item(x,y))

#for x in range(cols):
#    for y in range(fils):
#        p = img.itemset((x,y),10)
        #for dato in range():
#        fx = (float)((dx+0.5)*scale_x - 0.5)
#        sx = cvFloor(fx)
#        fx -= sx


#scale_x = 2
#dx = 1

#for x in range(cols):
#    for y in range(fils):
#        p = (float)((dx+0.5)*scale_x - 0.5)
        #p = img.itemset(x/scale_x,y/scale_x)
#        for i in range(i+1):
#            resultado= i<=p<i+1
#        p = p-resultado
        
#factor = 2
#W = img.getWidth()
#H = img.getHeight()
#newW = int(W*factor)
#newH = int(H*factor)
#newImage = img.EmptyImage(newW, newH)
#for cols in range(newW):
#    for fils in range(newH):
#      p = img.getPixel(cols/factor,fils/factor)
#      newImage.setPixel(cols,fils,p)

#cv2.imshow('salida.jpg',img)
