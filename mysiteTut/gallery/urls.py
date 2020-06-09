from django.urls import path, re_path , include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'gallery'
urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
    path('upload_image/thresholding',views.thresholding),
    path('upload_image/blending',views.blending),
    path('upload_image/raiz',views.raiz),
    path('upload_image/raiztopower',views.raiztopower),
    path('upload_image/Logaritmo',views.Logaritmo),
    #path('upload_image/Ecualizacion',views.Ecualizacion),
    path('upload_image/Exponencial',views.Exponencial),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
