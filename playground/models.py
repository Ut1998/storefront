from distutils.command.upload import upload
from statistics import mode
from django.db import models

# Create your models here.


class Storefront(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    img = models.ImageField(upload_to="pics", default="default.jpg")
