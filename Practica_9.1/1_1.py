import math
import random

import cv2
import numpy as np
from matplotlib import pyplot as plt


def Rotate(angulo,img):
    rows,cols, ch = img.shape
    c=math.sqrt(pow(rows,2)+pow(cols,2))
    ang_img=math.acos(-(pow(cols,2)-pow(rows,2)-pow(c,2))/(2*rows*c))
    print(ang_img)
    if math.pi/2<=(angulo%(2*math.pi))<math.pi:
        X=-c*math.sin(-angulo+ang_img)
        Y=-c*math.sin(math.pi/2+angulo+ang_img)
    elif math.pi<=(angulo%(2*math.pi))<math.pi*3/2:
        X=-c*math.sin(angulo+ang_img)
        Y=-c*math.sin(math.pi/2-angulo+ang_img)
    elif math.pi*3/2<=(angulo%(2*math.pi))<2*math.pi:
        X=c*math.sin(-angulo+ang_img)
        Y=c*math.sin(math.pi/2+angulo+ang_img)
    else:
        X=c*math.sin(angulo+ang_img)
        Y=c*math.sin(math.pi/2-angulo+ang_img)

    X1=math.ceil(X)
    X2=math.floor(X)
    Y1=math.ceil(Y)
    Y2=math.floor(Y)
    N=np.array([[1.,   0.,  cols],
                [0.,   1.,  rows]])
    img2 = cv2.warpAffine(img, N, (cols*3,rows*3))
    rows1,cols1, ch1 = img2.shape
    N=np.array([[math.cos(angulo)   ,   math.sin(angulo)    ,  (1-math.cos(angulo))*cols1/2   -   math.sin(angulo)      *rows1/2],
                [-math.sin(angulo)  ,   math.cos(angulo)    ,   math.sin(angulo)   *cols1/2   +   (1-math.cos(angulo))  *rows1/2]])
    img3 = cv2.warpAffine(img2, N, (cols*3,rows*3))
    q=(X1-cols)/2
    w=(Y1-rows)/2
    print(q,w)
    N=np.array([[1.,   0.,  -cols+q],
                [0.,   1.,  -rows+w]])
    print(X,Y)
    print((abs(X1),abs(Y1)))
    img4 = cv2.warpAffine(img3, N, (abs(X1),abs(Y1)))
    return img3,img4

img=cv2.imread('Touch_Me.jpg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows,cols, ch = img.shape
print(rows,cols)
img3,img2 = Rotate(math.pi/2,img)
plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.subplot(122)
plt.imshow(img2)
plt.title('Output')
plt.show()
img2=cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
cv2.imwrite('imagen_2.jpg',img2)
