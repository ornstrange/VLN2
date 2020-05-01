from django.db import models

# Create your models here.
class Product(models.Model):

    id = models.IntegerField("Id", primary_key = True)
    keywords = models.CharField("Keywords", max_length=50)
    image = models.ImageField("Image", upload_to=None, height_field=None, width_field=None, max_length=None)
    name = models.CharField("Name", max_length=50)
    desc = models.TextField("Description")
    type = models.CharField("Type", max_length=50)
    price = models.IntegerField("Price") 

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
