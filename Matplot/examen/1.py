### EJERCICIO 1

import cv2
import numpy as np
import matplotlib as plt

#en mi grupo usamos IMREAD_GRAYSCALE para trabajar las tareas
img = cv2.imread("question_1.png", cv2.IMREAD_GRAYSCALE)

#########  write your code here ##################

filas,columnas=img.shape
#A y B minimo y maximo
A=0
B=255
#lista con valores 0 para todos los valores de color
lista=[0]*256
lista2=[]
#numero de pixeles
total=filas*columnas

for x in range(filas):
    for y in range(columnas):
        #es una lista contador para cada valor de color, se suma 1 cada ves que encuentra el valor
        lista[img.item(x,y)]=lista[img.item(x,y)]+1

#ponemos todos los valores incluyendo repeticiones en una lista para tomar por porcentaje el limite de donde se tomara el equalization
for i in range(len(lista)):
    lista2=lista2+[i]*lista[i]

#porcentaje de menor y menor para toar
x=5*total/100
y=95*total/100
#elejimos de donde tomara valores
C=lista2[round(x)]
D=lista2[round(y)]
#empieza el reeplaso de valores
for x in range(filas):
    for y in range(columnas):
        #formula de clase
        t=(img.item(x,y)-C)*((B-A)/(D-C))+A
        if t<0:
            t=0
        if t>255:
            t=255     
        img.itemset((x,y),t)
img_out = img

######## the result have to be set in img_out ####
######## not modify from here ####################

cv2.imwrite("question_1_sol.png", img_out)
