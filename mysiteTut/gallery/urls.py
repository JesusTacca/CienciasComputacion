from django.urls import path, re_path , include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'gallery'
urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
    path('upload_image/thresholding',views.thresholding),
    path('upload_image/mostrar1',views.mostrar1),
    path('upload_image/mostrar2',views.mostrar2),
    path('upload_image/mostrar3',views.mostrar3),
    path('upload_image/mostrar4',views.mostrar4),
    path('upload_image/mostrar5',views.mostrar5),
    path('upload_image/mostrar6',views.mostrar6),
    path('upload_image/mostrar7',views.mostrar7),
    path('upload_image/mostrar8',views.mostrar8),
    path('upload_image/mostrar9',views.mostrar9),
    path('upload_image/mostrar10',views.mostrar10),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
