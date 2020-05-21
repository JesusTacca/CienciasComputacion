from django.shortcuts import render
import cv2
import math
from matplotlib import pyplot as plt
import io
import urllib, base64
from .forms import *
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
global jug
jug='como_lo_supiste.jpg'
def home(request):
    return render(request,'home.html')#,{'data':urls})
def thresholding(request):
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    fils,cols=img.shape
    for x in range(fils):
        for y in range(cols):
            if img.item(x,y)<=194 and 175<=img.item(x,y):
                img2.itemset((x, y), 255)
            else:
                img2.itemset((x, y), 0)
    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'thresholding.html',{'data':uri})

def Contrast(request):
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
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
    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'contrast.html',{'data':uri})

def Ecualizacion(request):
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
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
    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'ecualizacion.html',{'data':uri})

def Logaritmo(request):
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
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
    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'logarithm.html',{'data':uri})

def Raiz(request):
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
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

    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request,'raiz.html',{'data':uri})

def Exponencial(request):
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
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
    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()

    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'exponencial.html',{'data':uri})

def raisepower(request):
    img=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/images/'+jug, cv2.IMREAD_GRAYSCALE)
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
    plt.imshow(img2,'gray')
    #plt.plot(range(10))
    fig =plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request,'raisetopower.html',{'data':uri})

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
    return HttpResponse('Subido Correctamente')
