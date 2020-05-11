from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from products.models import Product
from user.models import User

class Cart(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             on_delete=models.SET_NULL)
    status = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField(default=0,
                                      blank=True)

class Cart_item(models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                on_delete=models.SET_NULL)
    total_price = models.IntegerField(default=0,
                                      blank=True)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart',
                             on_delete=models.CASCADE)

@receiver(pre_save, sender=Cart_item)
def calc_total_price(sender, instance, **kwargs):
    instance.total_price = instance.product.price * instance.quantity

@receiver(post_save, sender=Cart_item)
def update_cart_price(sender, instance, created, **kwargs):
    if created:
        instance.cart.total_price += instance.total_price
        instance.cart.save()

