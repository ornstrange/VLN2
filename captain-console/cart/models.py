from django.db import models
from products.models import Product
from user.models import User

# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)