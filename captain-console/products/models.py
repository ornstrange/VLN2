from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key = True)
    keywords = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
<<<<<<< HEAD
    desc = models.TextField()
    type = models.CharField(max_length=50)
    price = models.IntegerField()

=======
    description = models.CharField(blank=True)
    categorie = models.CharField(max_length=50)
    price = models.IntegerField()
>>>>>>> 6d977f68f2e61f0e3a8ca094a83b35dcdcd397f3
