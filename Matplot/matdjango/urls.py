from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('ecualizar',views.funct1),
    path('contrastar',views.funct2),
    path('logaritmear',views.funct3),
    path('exponenciar',views.funct4),
    path('home',views.home),
]
