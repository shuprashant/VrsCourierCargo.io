from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
