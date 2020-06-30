import numpy as np
import math
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('drawing.png')
rows,cols,ch = img.shape
def getAffine(A,B):
    A=np.float32([ [A[0][0],A[0][1],1] , [A[1][0],A[1][1],1] , [A[2][0],A[2][1],1] ])
    A=A.T
    A=np.linalg.inv(A)
    B = B.T
    MATR = B.dot(A)
    return MATR

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)
N=getAffine(pts1,pts2)

dst1 = cv2.warpAffine(img,M,(cols,rows))
dst2 = cv2.warpAffine(img,N,(cols,rows))

plt.subplot(121),plt.imshow(dst1),plt.title('OpenCV')
plt.subplot(122),plt.imshow(dst2),plt.title('MANUAL')
plt.show()
