import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

def translacion(X,Y,img):
    N=np.array([[1.,0.,X],[0.,1.,Y]])
    rows,cols, ch = img.shape
    img2 = cv2.warpAffine(img, N, (cols, rows))
    return img2
def escala(X,Y,img):
    N=np.array([[X,0.,0],[0.,Y,0]])
    rows,cols, ch = img.shape
    img2 = cv2.warpAffine(img, N, (cols, rows))
    return img2
def Rotate(angulo,img):
    rows,cols, ch = img.shape
    N=np.array([[math.cos(angulo)   ,   math.sin(angulo)    ,  (1-math.cos(angulo))*cols/2   -   math.sin(angulo)      *rows/2],
                [-math.sin(angulo)  ,   math.cos(angulo)    ,   math.sin(angulo)    *cols/2   +   (1-math.cos(angulo))  *rows/2]])
    img2 = cv2.warpAffine(img, N, (cols, rows))
    return img2
def Shear(X1,X2,Y1,Y2,img):
    rows,cols, ch = img.shape
    N=np.array([[X1,Y1,0],
                [X2,Y2,0]])
    img2 = cv2.warpAffine(img, N, (cols, rows))
    return img2

img=cv2.imread('imagen_1.jpg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#img2 = translacion(50,150,img)
#img2 = escala(0.4,0.8,img)
img2 = Rotate(math.pi/2,img)
#img2 = Shear(0.2,0.9,0.5,0.5,img)
plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.subplot(122)
plt.imshow(img2)
plt.title('Output')
plt.show()

img2=cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
cv2.imwrite('imagen_2.jpg',img2)