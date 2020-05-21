from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('thresholding',views.thresholding),
    path('Contrast',views.Contrast),
    path('Ecualizacion',views.Ecualizacion),
    path('Logaritmo',views.Logaritmo),
    path('Raiz',views.Raiz),
    path('Exponencial',views.Exponencial),
    path('topower',views.raisepower),
    path('home',views.home),
    path('image_upload', views.image_upload, name = 'image_upload'),
    path('success', views.success, name = 'success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
