from django.shortcuts import render
import cv2
import math
from matplotlib import pyplot as plt
import io
import urllib, base64

def home(request):
    img=cv2.imread('matdjango/Imagenes/log_1.jpg', cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread('matdjango/Imagenes/log_1.jpg', cv2.IMREAD_GRAYSCALE)
    fils,cols=img.shape
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
    return render(request,'home.html',{'data':uri})
