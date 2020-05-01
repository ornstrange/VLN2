from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key = True)
    keywords = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    type = models.CharField(max_length=50)
    price = models.IntegerField()

