import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

def binP(num):
    b_num = bin(num)
    b_num2 = b_num[slice(2,len(b_num),1)]
    return b_num2
def deci(num):
    rango = len(num)
    value = 0
    for i in range(rango):
            digit = num[rango-i-1]
            if digit == '1':
                    value = value + pow(2, i)
    return value
def andB(num1,num2):
    len1=len(num1)
    len2=len(num2)
    if len1 < len2:
        rest = len2-len1
        for i in range (rest):
            num1 = num1 + '0'
    elif len2 < len1:
        rest = len1-len2
        for i in range (rest):
            num2 = num2 + '0'
    rango = len(num1)

    value = ''
    
    for i in range (0,rango):
        if(num1[rango-1-i] == '1' and num2[rango-1-i] == '1' ):
            value = '1' + value
        else:
            value = '0' + value
    return value


img=cv2.imread('log_3.png')
img2=cv2.imread('log_4.png')
a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))

for x in range(a):
    for y in range(b):
        img.itemset( (x,y,0),deci( andB( binP(img.item(x,y,0)) , binP(img2.item(x,y,0)) ) ) )
        img.itemset( (x,y,1),deci( andB( binP(img.item(x,y,1)) , binP(img2.item(x,y,1)) ) ) )
        img.itemset( (x,y,2),deci( andB( binP(img.item(x,y,2)) , binP(img2.item(x,y,2)) ) ) )

cv2.imwrite('AND.jpg',img)
#img=cv2.imread('AND.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.imwrite('AND.jpg',img)






