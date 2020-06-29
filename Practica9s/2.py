import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gran-dragon-mitologia.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,250],[0,1,150]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
