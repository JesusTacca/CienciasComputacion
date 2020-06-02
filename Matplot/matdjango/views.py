from django.shortcuts import render
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
import io
import urllib, base64
from .forms import *
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
global jug


jug='neko113.jpg'


#retorno a pagina de inicio
def home(request):
    return render(request,'home.html')#,{'data':urls})


#Funcion thresholding por defecto
def thresholding(request):
    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #funcion de thresholding
    fils,cols=img.shape
    for x in range(fils):
        for y in range(cols):
            if img.item(x,y)<=194 and 175<=img.item(x,y):
                img2.itemset((x, y), 255)
            else:
                img2.itemset((x, y), 0)
    #fin de la funcion

    plt.imshow(img2,'gray')

    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualizar la pagina de la funcion
    return render(request,'thresholding.html',{'data':uri})

#funcion customisada de thresholding
def thre1(request):
    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #lectura de variables
    fils,cols=img.shape
    a=int(request.POST['valor1'])
    b=int(request.POST['valor2'])

    #funcion thresholding
    for x in range(fils):
        for y in range(cols):
            if img.item(x,y)<=b and a<=img.item(x,y):
                img2.itemset((x, y), 255)
            else:
                img2.itemset((x, y), 0)
    #fin de la funcion

    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    cv2.imwrite('matdjango/Imagenes/images/temp.jpg',img2)
    print(12345659)

    #actualizar la pagina de la funcion
    return render(request,'thresholding.html',{'data':uri})

def Contrast(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #funcion contrast stretching
    a=0
    b=255
    c=255
    d=0
    fils,cols=img2.shape
    for x in range(fils):
        for y in range(cols):
            if c>img2.item(x,y):
                c=img2.item(x,y)
            if d<img2.item(x,y):
                d=img2.item(x,y)
    for x in range(fils):
        for y in range(cols):
            t=(img2.item(x,y)-c)*((b-a)/(d-c))+a
            img2.itemset((x, y), t)
    #fin de la funcion

    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'contrast.html',{'data':uri})

def Contrast_custom(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #lectura de variables
    a=0
    b=255
    print(request.POST['valor1'])
    print(request.POST['valor2'])
    min=int(request.POST['valor1'])
    max=int(request.POST['valor2'])
    fils,cols=img2.shape

    lista=[0]*256
    cont=fils*cols

    #funcion contrast stretching customisada
    for x in range(fils):
        for y in range(cols):
            lista[img.item(x,y)]=lista[img.item(x,y)]+1

    lista2=[]
    for i in range(len(lista)):
        lista2=lista2+[i]*lista[i]
    print(len(lista2),cont)
    x=min*cont/100
    y=max*cont/100
    print(x,y)
    c=lista2[round(x)]
    d=lista2[round(y)]
    print(c,d)
    for x in range(fils):
        for y in range(cols):
            t=(img.item(x,y)-c)*((b-a)/(d-c))+a
            if t<0:
                t=0
            if t>255:
                t=255
            img2.itemset((x, y), t)
    #fin de la funcion


    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'contrast.html',{'data':uri})

def Ecualizacion(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #funcion Ecualizacion
    fils,cols=img2.shape
    lista=[0]*256
    cont=fils*cols
    for x in range(fils):
        for y in range(cols):
            lista[img2.item(x,y)]=lista[img2.item(x,y)]+1

    L=256
    pp=[0]*256
    for i in range (256):
        pp[i]=lista[i]/cont
    nueva=[0]*256
    for i in range (256):
        suma=0
        for j in range(i+1):
            suma=suma+pp[j]
        suma=math.floor(suma*(L-1))
        nueva[i]=suma

    for x in range(fils):
        for y in range(cols):
            img2.itemset((x,y),nueva[img2.item(x,y)])
    #fin de la funcion


    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'ecualizacion.html',{'data':uri})

def Ecualizacion_custom(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #lectura de variables
    a=int(request.POST['valorx1'])
    b=int(request.POST['valorx2'])
    c=int(request.POST['valory1'])
    d=int(request.POST['valory2'])
    fils,cols=img.shape
    lista=[0]*256
    cont=fils*cols

    croppedImage = img[c:d, a:b]
    img3= cv2.resize(croppedImage, (cols, fils))
    #cv2.imwrite('prueba4.jpg',img3)

    #funcion Ecualizacion customisada
    for x in range(fils):
        for y in range(cols):
            lista[img3.item(x,y)]=lista[img3.item(x,y)]+1

    L=256
    pp=[0]*256
    for i in range (256):
        pp[i]=lista[i]/cont
    nueva=[0]*256
    print(sum(pp))
    for i in range (256):
        suma=0
        for j in range(i+1):
            suma=suma+pp[j]
        suma=math.floor(suma*(L-1))
        nueva[i]=suma

    for x in range(fils):
        for y in range(cols):
            img2.itemset((x,y),nueva[img.item(x,y)])
    #fin de la funcion


    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'ecualizacion.html',{'data':uri})

def Logaritmo(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #funcion logarithm
    fils,cols=img.shape
    cont=fils*cols
    p=[0]*256
    c=70
    for x in range(fils):
        for y in range(cols):
            p=c*math.log(1+img.item(x,y),10)
            if p>255:
                p=255
            if p<0:
                p=0
            img2.itemset((x,y),int(p))
    #fin de la funcion

    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'logarithm.html',{'data':uri})

def Logaritmo_custom(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #lectura de variables
    c=int(request.POST['valorC'])

    #funcion Logaritmo customisada
    fils,cols=img.shape
    cont=fils*cols
    p=[0]*256
    for x in range(fils):
        for y in range(cols):
            p=c*math.log(1+img.item(x,y),10)
            if p>255:
                p=255
            if p<0:
                p=0
            img2.itemset((x,y),int(p))
    #fin de la funcion

    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'logarithm.html',{'data':uri})

def Raiz(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)


    #funcion raiz
    fils,cols=img.shape
    cont=fils*cols
    p=[0]*256
    c=40
    for x in range(fils):
        for y in range(cols):
            p=c*math.sqrt(img.item(x,y))
            if p>255:
                p=255
            if p<0:
                p=0
            img2.itemset((x,y),int(p))
    #fin de la funcion

    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'raiz.html',{'data':uri})

def Raiz_custom(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #lectura de las variables
    c=int(request.POST['valorC'])

    #funcion raiz customisada
    fils,cols=img.shape
    cont=fils*cols
    p=[0]*256
    for x in range(fils):
        for y in range(cols):
            p=c*math.sqrt(img.item(x,y))
            if p>255:
                p=255
            if p<0:
                p=0
            img2.itemset((x,y),int(p))
    #fin de la funcion


    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'raiz.html',{'data':uri})

def Exponencial(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #funcion exponencial
    fils,cols=img.shape
    cont=fils*cols
    p=[0]*256
    c=20
    b=1.01
    for x in range(fils):
        for y in range(cols):
            p=c*(pow(b,img.item(x,y))-1)
            if p>255:
                p=255
            if p<0:
                p=0
            img2.itemset((x,y),int(p))
    #fin de la funcion

    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'exponencial.html',{'data':uri})

def Exponencial_custom(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #lectura de variables
    c=int(request.POST['valorC'])

    #funcion Exponencial customisada
    b=1.01
    fils,cols=img.shape
    cont=fils*cols
    p=[0]*256
    for x in range(fils):
        for y in range(cols):
            p=c*(pow(b,img.item(x,y))-1)
            if p>255:
                p=255
            if p<0:
                p=0
            img2.itemset((x,y),int(p))
    #fin de la funcion

    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'exponencial.html',{'data':uri})

def raisepower(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #funcion raisepower
    fils,cols=img.shape
    cont=fils*cols
    p=[0]*256
    c=0.1
    r=1.5
    for x in range(fils):
        for y in range(cols):
            p=c*pow(img.item(x,y),r)
            if p>255:
                p=255
            if p<0:
                p=0
            img2.itemset((x,y),int(p))
    #in de la funcion


    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'raisetopower.html',{'data':uri})

def raisepower_custom(request):

    #lectura de imagenes
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)

    #lectura de variables
    c=int(request.POST['valorC'])

    #funcion raisepower customisada
    p=[0]*256
    r=1.5
    fils,cols=img.shape
    cont=fils*cols
    for x in range(fils):
        for y in range(cols):
            p=c*pow(img.item(x,y),r)
            if p>255:
                p=255
            if p<0:
                p=0
            img2.itemset((x,y),int(p))
    #fin de la funcion


    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    #actualiza la pagina de la funcion
    return render(request,'raisetopower.html',{'data':uri})
def addition(request):
    img=cv2.imread('matdjango/Imagenes/images/'+'add_2.jpg')
    img2=cv2.imread('matdjango/Imagenes/images/'+'add_1.jpg')
    a=max(len(img),len(img2))
    b=max(len(img[0]),len(img2[0]))
    img=cv2.resize(img,(b,a))
    img2=cv2.resize(img2,(b,a))
    for x in range(a):
        for y in range(b):
            p=int(img.item(x,y,0)/2+img2.item(x,y,0)/2)
            img.itemset((x,y,0),p)
            p=int(img.item(x,y,1)/2+img2.item(x,y,1)/2)
            img.itemset((x,y,1),p)
            p=int(img.item(x,y,2)/2+img2.item(x,y,2)/2)
            img.itemset((x,y,2),p)
    plt.imshow(img)
    #plt.plot(range(10))
    fig =plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'addition.html',{'data':uri})
def addition1(request):
    img=cv2.imread('matdjango/Imagenes/images/'+'add_2.jpg')
    img2=cv2.imread('matdjango/Imagenes/images/'+'add_1.jpg')
    a=max(len(img),len(img2))
    b=max(len(img[0]),len(img2[0]))
    img=cv2.resize(img,(b,a))
    img2=cv2.resize(img2,(b,a))
    for x in range(a):
        for y in range(b):
            p=int(img.item(x,y,0)/2+img2.item(x,y,0)/2)
            img.itemset((x,y,0),p)
            p=int(img.item(x,y,1)/2+img2.item(x,y,1)/2)
            img.itemset((x,y,1),p)
            p=int(img.item(x,y,2)/2+img2.item(x,y,2)/2)
            img.itemset((x,y,2),p)
    plt.imshow(img)
    #plt.plot(range(10))
    fig =plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'addition.html',{'data':uri})
def subtraction(request):
    img=cv2.imread('matdjango/Imagenes/images/'+'add_2.jpg')
    img2=cv2.imread('matdjango/Imagenes/images/'+'add_1.jpg')
    a=max(len(img),len(img2))
    b=max(len(img[0]),len(img2[0]))
    img=cv2.resize(img,(b,a))
    img2=cv2.resize(img2,(b,a))
    for x in range(a):
        for y in range(b):
            p=(img.item(x,y,0)-img2.item(x,y,0))
            if p<0:
                img.itemset((x,y,0),0)
            else:
                img.itemset((x,y,0),p)
            p=(img.item(x,y,1)-img2.item(x,y,1))
            if p<0:
                img.itemset((x,y,1),0)
            else:
                img.itemset((x,y,1),p)
            p=(img.item(x,y,2)-img2.item(x,y,2))
            if p<0:
                img.itemset((x,y,2),0)
            else:
                img.itemset((x,y,2),p)
    plt.imshow(img)
    #plt.plot(range(10))
    fig =plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'subtraction.html',{'data':uri})
def subtraction1(request):
    img=cv2.imread('matdjango/Imagenes/images/'+'add_2.jpg')
    img2=cv2.imread('matdjango/Imagenes/images/'+'add_1.jpg')
    a=max(len(img),len(img2))
    b=max(len(img[0]),len(img2[0]))
    img=cv2.resize(img,(b,a))
    img2=cv2.resize(img2,(b,a))
    for x in range(a):
        for y in range(b):
            p=(img.item(x,y,0)-img2.item(x,y,0))
            if p<0:
                img.itemset((x,y,0),0)
            else:
                img.itemset((x,y,0),p)
            p=(img.item(x,y,1)-img2.item(x,y,1))
            if p<0:
                img.itemset((x,y,1),0)
            else:
                img.itemset((x,y,1),p)
            p=(img.item(x,y,2)-img2.item(x,y,2))
            if p<0:
                img.itemset((x,y,2),0)
            else:
                img.itemset((x,y,2),p)
    plt.imshow(img)
    #plt.plot(range(10))
    fig =plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'subtraction.html',{'data':uri})
def image_upload(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'home.html', {'form' : form})


def success(request):
    return render(request, 'home.html')
    #return HttpResponse('Subido Correctamente')
