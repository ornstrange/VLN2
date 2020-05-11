from django.shortcuts import render, redirect
from products.models import Product
from user.models import Customer
from cart.models import Cart, Cart_item

def index(request):
    cart = request.user.customer.active_cart
    cart_items = Cart_item.objects.filter(cart=cart) if cart else None
    context = {
        'cart': cart,
        'cart_items': cart_items
    }
    return render(request, 'cart/index.html', context=context)

def checkout(request):
    return render(request, 'cart/checkout.html')

def add(request):
    if request.user.is_authenticated:
        prod_id = request.POST.get('id')
        quantity = request.POST.get('quantity') or 1
        if type(quantity) == str:
            quantity = int(quantity) if quantity.isnumeric() else 1
        prod = Product.objects.get(pk=prod_id)
        customer = request.user.customer
        if customer.active_cart: # has active cart
            cart_item = Cart_item(quantity=quantity,
                                  product=prod,
                                  cart=customer.active_cart)
            cart_item.save()
        else: # create one
            new_cart = Cart(user=request.user,
                            status='Active')
            new_cart.save()
            cart_item = Cart_item(quantity=quantity,
                                  product=prod,
                                  cart=new_cart)
            cart_item.save()
            customer.active_cart = new_cart
            customer.save()
        return redirect('product', prod.id)
    else:
        return redirect('product', prod.id)

