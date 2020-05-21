from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('ecualizar',views.funct1),
    path('contrastar',views.funct2),
    path('logaritmear',views.funct3),
    path('exponenciar',views.funct4),
    path('home',views.home),
    path('image_upload', views.hotel_image_view, name = 'image_upload'),
    path('success', views.success, name = 'success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
