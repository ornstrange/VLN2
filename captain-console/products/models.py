from django.db import models

# Create your models here.
class Product(models.Model):

    id = models.IntegerField(primary_key = True)
    keywords = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    type = models.CharField(max_length=50)
    price = models.IntegerField() 

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
