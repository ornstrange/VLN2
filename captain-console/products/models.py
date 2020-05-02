from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key = True)
    keywords = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
<<<<<<< HEAD
    description = models.CharField(blank=True)
    categorie = models.CharField(max_length=50)
    price = models.IntegerField()
=======
    desc = models.TextField()
    type = models.CharField(max_length=50)
    price = models.IntegerField()

>>>>>>> 5120e9fd1f8c532756bb8dc6f34a574bbb4d1a1e
