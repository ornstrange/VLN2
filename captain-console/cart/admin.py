from django.contrib import admin
from cart.models import Cart, Cart_item, Contact_info, Payment_info, Order

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Cart_item)
admin.site.register(Contact_info)
admin.site.register(Payment_info)

