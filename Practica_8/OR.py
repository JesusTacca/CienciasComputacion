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
def OR(num1,num2):
    len1=len(num1)
    len2=len(num2)
    if len1 < len2:
        rest = len2-len1
        for i in range (rest):
            num1 = '0' + num1
    elif len2 < len1:
        rest = len1-len2
        for i in range (rest):
            num2 = '0' + num2
    rango = len(num1)

    value = ''
    
    for i in range (0,rango):
        if(num1[rango-1-i] == '0' and num2[rango-1-i] == '0' ):
            value = '0' + value
        else:
            value = '1' + value
    return value

img=cv2.imread('log_3.png')
img2=cv2.imread('log_4.png')
a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv2.resize(img,(b,a))
img2=cv2.resize(img2,(b,a))

for x in range(a):
    for y in range(b):
        img.itemset( (x,y,0),deci( OR( binP(img.item(x,y,0)) , binP(img2.item(x,y,0)) )  ))
        img.itemset( (x,y,1),deci( OR( binP(img.item(x,y,1)) , binP(img2.item(x,y,1)) )  ))
        img.itemset( (x,y,2),deci( OR( binP(img.item(x,y,2)) , binP(img2.item(x,y,2)) )  ))

cv2.imshow('OR.jpg',img)

