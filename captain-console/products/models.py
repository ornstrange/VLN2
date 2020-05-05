from django.urls import reverse
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    keywords = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    @property
    def thumbimg(self):
        return self.imglist[0]

    @property
    def imglist(self):
        return list(map(lambda x: f"{x}.jpg", self.image.split(';')))

    def __str__(self):
        return f"{self.id}: {self.name} / {self.category}"

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])

