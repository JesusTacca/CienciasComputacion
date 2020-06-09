from django import forms
from django.http import JsonResponse
from django.views.generic import TemplateView,ListView,View, CreateView, UpdateView
from .models import *
class ImageForm(forms.ModelForm):
   class Meta:
      model = Image
      fields = ['image','image2','name','name2']
