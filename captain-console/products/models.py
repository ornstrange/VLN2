from django.db import models

class Product(models.Model):
    keywords = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    description = models.CharField(blank=True)
    categorie = models.CharField(max_length=50)
    price = models.IntegerField()
