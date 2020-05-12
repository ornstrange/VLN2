from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django_countries.fields import CountryField
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

    def contains(self, product):
        all_items = Cart_item.objects.filter(cart=self)
        if all_items.filter(product=product):
            return all_items.get(product=product)
        else:
            return None

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

class Contact_info(models.Model):
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    country = CountryField()
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    house_nr = models.IntegerField()
    postcode = models.CharField(max_length=10)

class Payment_info(models.Model):
    last_four = models.CharField(max_length=4)
    expiration = models.CharField(max_length=7)
    cardholder = models.CharField(max_length=128)

class Order(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             on_delete=models.SET_NULL)
    cart = models.ForeignKey('Cart',
                             null=True,
                             on_delete=models.SET_NULL)
    contact = models.ForeignKey('Contact_info',
                                null=True,
                                on_delete=models.SET_NULL)
    payment = models.ForeignKey('Payment_info',
                                null=True,
                                on_delete=models.SET_NULL)
    status = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)

