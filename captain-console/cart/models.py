from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_delete
from products.models import Product
from user.models import User

class Cart(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             on_delete=models.SET_NULL)
    status = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        items = Cart_item.objects.filter(cart=self)
        return sum([i.total_price for i in items]) if items else 0

class Cart_item(models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart',
                             on_delete=models.CASCADE)

    @property
    def total_price(self):
        return self.quantity * self.product.price

@receiver(post_delete, sender='cart.Cart_item')
def delete_if_last(sender, instance, **kwargs):
    cart = instance.cart
    cart_items = Cart_item.objects.filter(cart=cart)
    if len(cart_items) == 0:
        cart.delete()

