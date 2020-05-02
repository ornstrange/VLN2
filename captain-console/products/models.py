from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    image_count = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(blank=True)
    keywords = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)

