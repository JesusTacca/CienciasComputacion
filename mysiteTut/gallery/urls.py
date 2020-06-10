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
    path('upload_image/multiplicacion',views.multiplicacion),
    path('upload_image/division',views.division),
    path('upload_image/contrast',views.contrast),
    path('upload_image/substracion',views.substracion),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
