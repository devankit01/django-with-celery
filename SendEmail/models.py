from email.mime import image
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.URLField(max_length=200, null=True, blank=True)