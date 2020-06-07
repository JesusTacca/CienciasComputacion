from django.shortcuts import render, redirect
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
from django.http import HttpResponse
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
imagen_act=[""]
pagina=[""]
###############################
def upload_image(request):
    if request.method == 'GET':
        temp1= Image.objects.all()
        for i in temp1:
            if i.name!=imagen_act[0]:
                Image.objects.filter(name=i.name).delete()
        temp= Image.objects.all()
        print(temp)
        for i in temp:
            print(i.image.url)
        return render(request, 'upload_image.html', {'imagenes': temp,'este':'/gallery/Imagenes/gallery/kilo.jpg','pagina':pagina[0]})
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            imagen_act[0]=str(request.POST['name'])
            form.save()
            return HttpResponseRedirect('/gallery/upload_image/')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form' : form})
#################################
def mostrar1(request):
    if request.method == 'GET':
        pagina[0]="0"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar2(request):
    if request.method == 'GET':
        pagina[0]="1"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar3(request):
    if request.method == 'GET':
        pagina[0]="2"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar4(request):
    if request.method == 'GET':
        pagina[0]="3"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar5(request):
    if request.method == 'GET':
        pagina[0]="4"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar6(request):
    if request.method == 'GET':
        pagina[0]="5"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar7(request):
    if request.method == 'GET':
        pagina[0]="6"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar8(request):
    if request.method == 'GET':
        pagina[0]="7"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar9(request):
    if request.method == 'GET':
        pagina[0]="8"
        return HttpResponseRedirect('/gallery/upload_image/')
def mostrar10(request):
    if request.method == 'GET':
        pagina[0]="9"
        return HttpResponseRedirect('/gallery/upload_image/')
###############################
def thresholding(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html')
    elif request.method == 'POST':
        muestra[0]="0"
        jug=Image.objects.filter(name=imagen_act[0])
        fr=""
        for i in jug:
            fr=i.image.url
        fr=fr[1:]
        print("--------------------")
        print(fr)
        print("--------------------")
        img=cv2.imread(fr)
        img2=cv2.imread(fr)

        Rxval=int(request.POST['Rxval'])
        Ryval=int(request.POST['Ryval'])
        Gxval=int(request.POST['Gxval'])
        Gyval=int(request.POST['Gyval'])
        Bxval=int(request.POST['Bxval'])
        Byval=int(request.POST['Byval'])

        #funcion de thresholding
        fils = len(img)
        cols = len(img[0])
        for x in range(fils):
            for y in range(cols):
                #RED
                if img.item(x,y,0)<=Rxval and Ryval<=img.item(x,y,0):
                    img2.itemset((x, y, 0), 255)
                else:
                    img2.itemset((x, y, 0), 0)
                #GREEN
                if img.item(x,y,1)<=Gxval and Gyval<=img.item(x,y,1):
                    img2.itemset((x, y, 1), 255)
                else:
                    img2.itemset((x, y, 1), 0)
                #BLUE
                if img.item(x,y,2)<=Bxval and Byval<=img.item(x,y,2):
                    img2.itemset((x, y, 2), 255)
                else:
                    img2.itemset((x, y, 2), 0)
        #fin de la funcion
        cv2.imwrite('gallery/Imagenes/gallery/kilo.jpg',img2)
        #actualizar la pagina de la funcion
        return HttpResponseRedirect('/gallery/upload_image/')
