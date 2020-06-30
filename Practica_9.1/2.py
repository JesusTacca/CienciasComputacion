import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

def wardaffine_2(img,N,sz):
    img2= np.zeros((sz[1],sz[0],3), np.uint8)
    rows, cols, ch = img.shape
    for i in range(rows):
        for j in range(cols):
            B=np.array([[j,i,1]])
            T=N.dot(B.T)
            T1=int(T[0])
            T2=int(T[1])
            if T1<sz[0] and T2<sz[1]:
                img2.itemset((T2,T1,0),img.item(i,j,0))
                img2.itemset((T2,T1,1),img.item(i,j,1))
                img2.itemset((T2,T1,2),img.item(i,j,2))
    return img2
img=cv2.imread('Touch_Me.jpg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows,cols, ch = img.shape
N=np.array([[0.8,0.2,15],
            [0.4,1.,150]])
img2 = cv2.warpAffine(img, N, (cols, rows))
img3 = wardaffine_2(img,N,[cols,rows])
plt.subplot(121)
plt.imshow(img2)
plt.title('Input')
plt.subplot(122)
plt.imshow(img3)
plt.title('Output')
plt.show()