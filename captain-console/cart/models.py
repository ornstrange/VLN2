from django.db import models
from products.models import Product
from user.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)

