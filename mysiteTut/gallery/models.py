from django.db import models
class Image(models.Model):
   image = models.ImageField(upload_to = 'gallery', default='gallery/static/images/no-img.jpg')
   image2 = models.ImageField(upload_to = 'gallery', default='gallery/static/images/no-img.jpg')
   name = models.CharField(max_length=200)
   name2 = models.CharField(max_length=100, default="")
