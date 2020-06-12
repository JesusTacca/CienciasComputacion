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

def binP(num):
    num = int(num)
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
            num1 = '0' + num1
    else:
        rest = len1-len2
        for i in range (rest):
            num2 = '0' + num2

    rango = len(num1)

    value = ''

    for i in range (0,rango):
        if(num1[rango-1-i] == '1' and num2[rango-1-i] == '1' ):
            value = '1' + value
        else:
            value = '0' + value
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
def notB(num):
    return 255-num
def orA(num):
    return 255-num
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
        return render(request, 'upload_image.html', {'imagenes': temp,'este':'/gallery/Imagenes/gallery/rpta.jpg','este1':'/gallery/Imagenes/gallery/rpta2.jpg','pagina':pagina[0]})
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
def ecualizacion(request):
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
    img2=cv2.imread(current1)
    a=int(request.POST['y1val'])
    b=int(request.POST['y2val'])
    c=int(request.POST['x1val'])
    d=int(request.POST['x2val'])
    fils=len(img)
    cols=len(img[0])
    lista=[[0]*256,[0]*256,[0]*256]
    cont=fils*cols
    croppedImage = img[c:d, a:b]
    img3= cv2.resize(croppedImage, (cols, fils))
    for x in range(fils):
        for y in range(cols):
            lista[0][img3.item(x,y,0)]=lista[0][img3.item(x,y,0)]+1
            lista[1][img3.item(x,y,1)]=lista[1][img3.item(x,y,1)]+1
            lista[2][img3.item(x,y,2)]=lista[2][img3.item(x,y,2)]+1
    L=256
    p=[[0]*256,[0]*256,[0]*256]
    for i in range (256):
        p[0][i]=lista[0][i]/cont
        p[1][i]=lista[1][i]/cont
        p[2][i]=lista[2][i]/cont
    nueva=[[0]*256,[0]*256,[0]*256]
    print([sum(i) for i in p])
    for i in range (256):
        suma=[0,0,0]
        for j in range(i+1):
            suma[0]=suma[0]+p[0][j]
            suma[1]=suma[1]+p[1][j]
            suma[2]=suma[2]+p[2][j]
        suma[0]=math.floor(suma[0]*(L-1))
        suma[1]=math.floor(suma[1]*(L-1))
        suma[2]=math.floor(suma[2]*(L-1))
        nueva[0][i]=suma[0]
        nueva[1][i]=suma[1]
        nueva[2][i]=suma[2]
    for x in range(fils):
        for y in range(cols):
            img2.itemset((x,y,0),nueva[0][img.item(x,y,0)])
            img2.itemset((x,y,1),nueva[1][img.item(x,y,1)])
            img2.itemset((x,y,2),nueva[2][img.item(x,y,2)])
    cv2.imwrite('gallery/Imagenes/gallery/rpta2.jpg',img3)
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img2)
    return HttpResponseRedirect('/gallery/upload_image/')

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
    a=max(len(img),len(img2))
    b=max(len(img[0]),len(img2[0]))
    img=cv2.resize(img,(b,a))
    img2=cv2.resize(img2,(b,a))
    A=0
    B=255
    c1=255
    d1=0
    c2=255
    d2=0
    c3=255
    d3=0
    for x in range(a):
        for y in range(b):

            p=(img.item(x,y,0)/img2.item(x,y,0))
            img.itemset((x,y,0),p*C)
            if c1>img.item(x,y,0):
                c1=img.item(x,y,0)
            if d1<img.item(x,y,0):
                d1=img.item(x,y,0)
            p=(img.item(x,y,1)/img2.item(x,y,1))
            img.itemset((x,y,1),p*C)
            if c2>img.item(x,y,1):
                c2=img.item(x,y,1)
            if d2<img.item(x,y,1):
                d2=img.item(x,y,1)
            p=(img.item(x,y,2)/img2.item(x,y,2))
            img.itemset((x,y,2),p*C)
            if c3>img.item(x,y,2):
                c3=img.item(x,y,2)
            if d3<img.item(x,y,2):
                d3=img.item(x,y,2)

    for x in range(a):
        for y in range(b):
            t=(img.item(x,y,0)-c1)*((B-A)/(d1-c1))+A
            img.itemset((x,y,0),t)
            t=(img.item(x,y,1)-c2)*((B-A)/(d2-c2))+A
            img.itemset((x,y,1),t)
            t=(img.item(x,y,2)-c3)*((B-A)/(d3-c3))+A
            img.itemset((x,y,2),t)
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
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')


def adicion(request):
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
            p=int(img.item(x,y,0)/2+img2.item(x,y,0)/2)
            img.itemset((x,y,0),p)
            p=int(img.item(x,y,1)/2+img2.item(x,y,1)/2)
            img.itemset((x,y,1),p)
            p=int(img.item(x,y,2)/2+img2.item(x,y,2)/2)
            img.itemset((x,y,2),p)
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')

def binari_and(request):
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
            img.itemset( (x,y,0),deci( andB( binP(img.item(x,y,0)) , binP(img2.item(x,y,0)) ) ) )
            img.itemset( (x,y,1),deci( andB( binP(img.item(x,y,1)) , binP(img2.item(x,y,1)) ) ) )
            img.itemset( (x,y,2),deci( andB( binP(img.item(x,y,2)) , binP(img2.item(x,y,2)) ) ) )
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')


def binari_nand(request):
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
            img.itemset( (x,y,0), notB( deci( andB( binP(img.item(x,y,0)) , binP(img2.item(x,y,0)) ) )  ))
            img.itemset( (x,y,1), notB( deci( andB( binP(img.item(x,y,1)) , binP(img2.item(x,y,1)) ) )  ))
            img.itemset( (x,y,2), notB( deci( andB( binP(img.item(x,y,2)) , binP(img2.item(x,y,2)) ) )  ))

    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')

def binari_or(request):
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
            img.itemset( (x,y,0),deci( OR( binP(img.item(x,y,0)) , binP(img2.item(x,y,0)) ) ) )
            img.itemset( (x,y,1),deci( OR( binP(img.item(x,y,1)) , binP(img2.item(x,y,1)) ) ) )
            img.itemset( (x,y,2),deci( OR( binP(img.item(x,y,2)) , binP(img2.item(x,y,2)) ) ) )
    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')


def binari_xor(request):
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
            img.itemset( (x,y,0), orA( deci( OR( binP(img.item(x,y,0)) , binP(img2.item(x,y,0)) ) )  ))
            img.itemset( (x,y,1), orA( deci( OR( binP(img.item(x,y,1)) , binP(img2.item(x,y,1)) ) )  ))
            img.itemset( (x,y,2), orA( deci( OR( binP(img.item(x,y,2)) , binP(img2.item(x,y,2)) ) )  ))

    cv2.imwrite('gallery/Imagenes/gallery/rpta.jpg',img)
    return HttpResponseRedirect('/gallery/upload_image/')
