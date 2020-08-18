from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import math
import numpy as np
import cv2
from django.http import HttpResponseRedirect


def home(request):
  if request.method == 'GET':
    return render(request, 'opencv_webapp/uimage.html', {})
  if request.method == 'POST':
    return render(request, 'opencv_webapp/uimage.html', {})

def boton(request):
    if request.method == 'GET':
      return render(request, 'opencv_webapp/boton.html', {})
    if request.method == 'POST':
      return render(request, 'opencv_webapp/boton.html', {})
