import cv2
import numpy as np
import math
import matplotlib as plt

img = cv2.imread("question_3.png",cv2.IMREAD_GRAYSCALE)

#########  write your code here ##################

#profe no me salio :'v estaba probando el codigo de la 1


filas,columnas=img.shape
c=180
for x in range(filas):
    for y in range(columnas):
        p=c*math.log(1+img.item(x,y),10)
        if p>255:
            p=255
        if p<0:
            p=0
        img.itemset((x,y),int(p))

#empieza el analizis
for x in range(filas):
    for y in range(columnas):
        #para poder determinar los valores se utiliza la legendaria tecnica del tanteo , las matematicas dan miedo...
        if img.item(x,y)<=235 and 47<=img.item(x,y):
            img.itemset((x, y), 255)
        else:
            img.itemset((x, y), 0)

#se que la imagen no esta bien ya que no toma alunos valores que considera negros al estar en una sona mas negra de la imagen, y el tiempo no ayudo .
img_out = img

######## the result have to be set in img_out ####
######## not modify from here ####################

cv2.imwrite("question_3_sol.png", img_out)
