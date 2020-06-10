from django.shortcuts import render, redirect
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
from django.http import HttpResponse
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
imagen_act=["",""]
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
        return render(request, 'upload_image.html', {'imagenes': temp,'este':'/gallery/Imagenes/gallery/rpta.jpg','pagina':pagina[0]})
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            imagen_act[0]=str(request.POST['name'])
            imagen_act[1]=str(request.POST['name2'])
            form.save()
            return HttpResponseRedirect('/gallery/upload_image/')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form' : form})

###############################
def thresholding(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    for i in jug:
        current1=i.image.url
    current1=current1[1:]
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)

    Rxval=int(request.POST['Rxval'])
    Ryval=int(request.POST['Ryval'])
    Gxval=int(request.POST['Gxval'])
    Gyval=int(request.POST['Gyval'])
    Bxval=int(request.POST['Bxval'])
    Byval=int(request.POST['Byval'])
    print(Rxval,Ryval,Gxval,Gyval,Bxval,Byval)
    #funcion de thresholding
    fils = len(img)
    cols = len(img[0])
    for x in range(fils):
        for y in range(cols):
            #RED
            if img.item(x,y,0)>=Rxval and Ryval<=img.item(x,y,0):
                img.itemset((x, y, 0), 255)
            else:
                img.itemset((x, y, 0), 0)
            #GREEN
            if img.item(x,y,1)>=Gxval and Gyval<=img.item(x,y,1):
                img.itemset((x, y, 1), 255)
            else:
                img.itemset((x, y, 1), 0)
            #BLUE
            if img.item(x,y,2)>=Bxval and Byval<=img.item(x,y,2):
                img.itemset((x, y, 2), 255)
            else:
                img.itemset((x, y, 2), 0)
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')
def blending(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    current2=""
    for i in jug:
        current1=i.image.url
        current2=i.image2.url
    current1=current1[1:]
    current2=current2[1:]
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    img2=cv2.imread(current2)
    a=max(len(img),len(img2))
    b=max(len(img[0]),len(img2[0]))
    img=cv2.resize(img,(b,a))
    img2=cv2.resize(img2,(b,a))
    C=float(request.POST['porcentaje'])
    print(C)
    for x in range(a):
        for y in range(b):
            x1=abs(math.floor(img.item(x,y,0)*(C))  +  math.floor(img2.item(x,y,0)*(1-C)))
            img.itemset((x,y,0),x1)
            x1=abs(math.floor(img.item(x,y,1)*(C))  +  math.floor(img2.item(x,y,1)*(1-C)))
            img.itemset((x,y,1),x1)
            x1=abs(math.floor(img.item(x,y,2)*(C))  +  math.floor(img2.item(x,y,2)*(1-C)))
            img.itemset((x,y,2),x1)
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')
def raiz(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    for i in jug:
        current1=i.image.url
    current1=current1[1:]
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    fils = len(img)
    cols = len(img[0])

    cont=fils*cols
    p=[0]*256
    c=int(request.POST['valors'])
    for x in range(fils):
        for y in range(cols):
            p=c*math.sqrt(img.item(x,y,0))
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,0),int(p))
            p=c*math.sqrt(img.item(x,y,1))
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,1),int(p))
            p=c*math.sqrt(img.item(x,y,2))
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,2),int(p))
    #fin de la funcion
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')
def raiztopower(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    for i in jug:
        current1=i.image.url
    current1=current1[1:]
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    fils = len(img)
    cols = len(img[0])

    cont=fils*cols
    p=[0]*256
    r=1.5
    c=float(request.POST['barl'])
    for x in range(fils):
        for y in range(cols):
            p=c*pow(img.item(x,y,0),r)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,0),int(p))
            p=c*pow(img.item(x,y,1),r)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,1),int(p))
            p=c*pow(img.item(x,y,2),r)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,2),int(p))
    #fin de la funcion
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')
def Logaritmo(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    for i in jug:
        current1=i.image.url
    current1=current1[1:]
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    fils = len(img)
    cols = len(img[0])
    c=int(request.POST['valorC'])
    for x in range(fils):
        for y in range(cols):
            p=c*math.log(1+img.item(x,y,0),10)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,0),int(p))
            p=c*math.log(1+img.item(x,y,1),10)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,1),int(p))
            p=c*math.log(1+img.item(x,y,2),10)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,2),int(p))
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')
#def Ecualizacion(request):

    #jug=Image.objects.filter(name=imagen_act[0])
    #current1=""
    #current2=""
    #for i in jug:
        #current1=i.image.url
        #current2=i.image2.url
    #current1=current1[1:]
    #current2=current2[1:]
    #img=cv2.imread(current1)
    #img2=cv2.imread(current2)
    #funcion Logaritmo customisada

def Exponencial(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    #current2=""
    for i in jug:
        current1=i.image.url
    current1=current1[1:]
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    fils = len(img)
    cols = len(img[0])
    c=int(request.POST['datoC'])
    b=1.01
    for x in range(fils):
        for y in range(cols):
            p=c*(pow(b,img.item(x,y,0))-1)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,0),int(p))
            p=c*(pow(b,img.item(x,y,1))-1)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,1),int(p))
            p=c*(pow(b,img.item(x,y,2))-1)
            if p>255:
                p=255
            if p<0:
                p=0
            img.itemset((x,y,2),int(p))
    #fin de la funcion
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')

def multiplicacion(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    for i in jug:
        current1=i.image.url
    current1=current1[1:]
    print("$$$$$$",request.POST,"$$$$$$$$")
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    a=len(img)
    b=len(img[0])
    c=int(request.POST['cval'])
    print("el C es ",c)
    for x in range(a):
        for y in range(b):

            p=int(img.item(x,y,0)*c)
            if p>255:
                p=255
            img.itemset((x,y,0),p)
            p=int(img.item(x,y,1)*c)
            if p>255:
                p=255
            img.itemset((x,y,1),p)
            p=int(img.item(x,y,2)*c)
            if p>255:
                p=255
            img.itemset((x,y,2),p)

    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')

def division(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    current2=""
    for i in jug:
        current1=i.image.url
        current2=i.image2.url
    current1=current1[1:]
    current2=current2[1:]
    C=int(request.POST['cval'])
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    img2=cv2.imread(current2)
    bimg1 = True
    bimg2 = True
    if np.any(img == None):
        bimg1 = False
    if np.any(img2 == None):
        bimg2 = False
    print(bimg1,bimg2,"estos son los resultados ")
    if np.logical_and(bimg1,bimg2):
        print("si hay")
        a=max(len(img),len(img2))
        b=max(len(img[0]),len(img2[0]))
        img=cv2.resize(img,(b,a))
        img2=cv2.resize(img2,(b,a))
        img2 = img
        nMax = 255
        nMin = 0
        Max = 0
        Min = 255
        for x in range(a):
            for y in range(b):
                if img2.item(x,y,0) == 0:
                    img2.item(x,y,0) == 1
                p=(img.item(x,y,0)/img2.item(x,y,0))
                img.itemset((x,y,0),p*C)
                if p <= Min:
                    Min = p
                if p >= Max:
                    Max = p
                if img2.item(x,y,1) == 0:
                    img2.item(x,y,1) == 1
                p=(img.item(x,y,1)/img2.item(x,y,1))
                img.itemset((x,y,1),p*C)
                if p <= Min:
                    Min = p
                if p >= Max:
                    Max = p
                if img2.item(x,y,2) == 0:
                    img2.item(x,y,2) == 1
                p=(img.item(x,y,2)/img2.item(x,y,2))
                img.itemset((x,y,2),p*C)
                if p <= Min:
                    Min = p
                if p >= Max:
                    Max = p
        Min=Min*C
        Max=Max*C
    else:
        print("entre aki")
        a=len(img)
        b=len(img[0])

        nMax = 255
        nMin = 0
        Max = 0
        Min = 255
        for x in range(a):
            for y in range(b):
                p=int(img.item(x,y,0)/C)
                img.itemset((x,y,0),p)
                if p <= Min:
                    Min = p
                if p >= Max:
                    Max = p
                p=int(img.item(x,y,1)/C)
                img.itemset((x,y,1),p)
                if p <= Min:
                    Min = p
                if p >= Max:
                    Max = p
                p=int(img.item(x,y,2)/C)
                img.itemset((x,y,2),p)
                if p <= Min:
                    Min = p
                if p >= Max:
                    Max = p
        Min=Min
        Max=Max

    rest = Max-Min
    if rest == 0:
        rest = 1
    for x in range(a):
        for y in range(b):
            p=int((((img.item(x,y,0)-(Min))*((nMax-nMin)/(rest)))+nMin))
            if p >= 255:
                p=255
            if p <= 0:
                p=0
            img.itemset((x,y,0),p)
            p=int((((img.item(x,y,1)-(Min))*((nMax-nMin)/(rest)))+nMin))
            if p >= 255:
                p=255
            if p <= 0:
                p=0
            img.itemset((x,y,1),p)
            p=int((((img.item(x,y,2)-(Min))*((nMax-nMin)/(rest)))+nMin))
            if p >= 255:
                p=255
            if p <= 0:
                p=0
            img.itemset((x,y,2),p)
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')

def contrast(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    for i in jug:
        current1=i.image.url
    current1=current1[1:]
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    img2=cv2.imread(current1)
    fils=len(img)
    cols=len(img[0])
    xval=int(request.POST['xval'])
    yval=int(request.POST['yval'])
    a=0
    b=255
    lista=[0]*256
    cont=fils*cols
    for x in range(fils):
        for y in range(cols):
            lista[img2.item(x,y,0)]=lista[img2.item(x,y,0)]+1
            lista[img2.item(x,y,1)]=lista[img2.item(x,y,1)]+1
            lista[img2.item(x,y,2)]=lista[img2.item(x,y,1)]+1
    lista2=[]
    for i in range(len(lista)):
        lista2=lista2+[i]*lista[i]
    x=xval*cont/100
    y=yval*cont/100
    c=lista2[round(x)]
    d=lista2[round(y)]

    for x in range(fils):
        for y in range(cols):
            t=(img.item(x,y,0)-c)*((b-a)/(d-c))+a
            if t<0:
                t=0
            if t>255:
                t=255
            img2.itemset((x, y,0), t)
            t=(img.item(x,y,1)-c)*((b-a)/(d-c))+a
            if t<0:
                t=0
            if t>255:
                t=255
            img2.itemset((x, y,1), t)
            t=(img.item(x,y,2)-c)*((b-a)/(d-c))+a
            if t<0:
                t=0
            if t>255:
                t=255
            img2.itemset((x, y,2), t)
    img = img2
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')

def substracion(request):
    jug=Image.objects.filter(name=imagen_act[0])
    current1=""
    current2=""
    for i in jug:
        current1=i.image.url
        current2=i.image2.url
    current1=current1[1:]
    current2=current2[1:]
    if 'cascade' in request.POST:
        if str(request.POST['cascade'])=="on":
            current1="gallery/Imagenes/gallery/rpta.jpg"
    img=cv2.imread(current1)
    img2=cv2.imread(current2)
    a=max(len(img),len(img2))
    b=max(len(img[0]),len(img2[0]))
    img=cv2.resize(img,(b,a))
    img2=cv2.resize(img2,(b,a))
    for x in range(a):
        for y in range(b):
            p=abs(img.item(x,y,0)-img2.item(x,y,0)-100)
            img.itemset((x,y,0),p)
            p=abs(img.item(x,y,1)-img2.item(x,y,1)-100)
            img.itemset((x,y,1),p)
            p=abs(img.item(x,y,2)-img2.item(x,y,2)-100)
            img.itemset((x,y,2),p)
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')
