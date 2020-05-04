from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    keywords = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)

    @property
    def thumbimg(self):
        return self.image.split(";")[0] + ".jpg"

