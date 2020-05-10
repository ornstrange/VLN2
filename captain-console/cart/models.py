from django.db import models
from products.models import Product
from user.models import User

class Cart(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             on_delete=models.SET_NULL)
    status = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)

class Cart_item(models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                on_delete=models.SET_NULL)
    total_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart,
                             on_delete=models.CASCADE)

