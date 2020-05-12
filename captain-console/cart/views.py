from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product
from user.models import Customer
from cart.models import Cart, Cart_item

@login_required
def index(request):
    cart = request.user.customer.active_cart
    cart_items = Cart_item.objects.filter(cart=cart) if cart else None
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'style': 'cart.css'
    }
    return render(request, 'cart/index.html', context=context)

def checkout(request):
    return render(request, 'cart/checkout.html')

@login_required
def add_quantity(request):
    cart_item_id = request.POST.get('id')
    cart_item = Cart_item.objects.get(pk=cart_item_id)
    if cart_item.quantity < 10:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.error(request, f"You can't have more than ten of this item.")
    return redirect('cart')

@login_required
def dec_quantity(request):
    cart_item_id = request.POST.get('id')
    cart_item = Cart_item.objects.get(pk=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        messages.error(request, f"You can't have less than one of this item.")
        messages.error(request, f"Please delete it if you want to remove it.")
    return redirect('cart')

@login_required
def delete(request):
    customer = request.user.customer
    if customer.active_cart:
        # delete item from cart
        cart_item_id = request.POST.get('id')
        cart_item = Cart_item.objects.get(pk=cart_item_id)
        if cart_item:
            msg = f"{cart_item.product.name} has been removed from your cart."
            messages.warning(request, msg)
            cart_item.delete()
        return redirect('cart')

@login_required
def add(request):
    # add item to cart
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
    messages.info(request, f"{prod.name} has been added to your cart.")
    return redirect(prod)

