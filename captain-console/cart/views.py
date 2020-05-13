from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from products.models import Product
from user.models import Customer
from cart.models import Cart, Cart_item, Contact_info, Payment_info, Order
from cart.forms import Contact_info_form, Payment_info_form

# Cart
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

@login_required
def add_quantity(request):
    if request.method == "GET":
        raise Http404()
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
    if request.method == "GET":
        raise Http404()
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
    if request.method == "GET":
        raise Http404()
    customer = request.user.customer
    if customer.active_cart:
        # delete item from cart
        cart_item_id = request.POST.get('id')
        if Cart_item.objects.filter(pk=cart_item_id):
            cart_item = Cart_item.objects.get(pk=cart_item_id)
            msg = f"{cart_item.product.name} has been removed from your cart."
            messages.warning(request, msg)
            cart_item.delete()
        return redirect('cart')

@login_required
def add(request):
    # add item to cart
    if request.method == "GET":
        raise Http404()
    prod_id = request.POST.get('id')
    quantity = request.POST.get('quantity') or 1
    if type(quantity) == str:
        quantity = int(quantity) if quantity.isnumeric() else 1
    prod = Product.objects.get(pk=prod_id)
    customer = request.user.customer
    if customer.active_cart: # has active cart
        if found := customer.active_cart.contains(prod):
            found.quantity += quantity
            if found.quantity > 10:
                found.quantity = 10
            found.save()
        else:
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

# Checkout
@login_required
def checkout(request):
    if request.user.customer.active_cart:
        if request.method == "POST":
            form = Contact_info_form(data=request.POST)
            if form.is_valid():
                contact_info = form.save()
                return redirect('checkout_payment',
                                cid=contact_info.id)
            else:
                messages.error(request, 'Invalid information...')
                messages.error(request, form.errors)
        context = {
            'form': Contact_info_form(),
            'style': 'checkout.css',
            'script': 'checkout.js'
        }
        return render(request, 'cart/checkout.html', context)
    else:
        raise Http404()

@login_required
def checkout_payment(request, cid=None):
    if request.user.customer.active_cart:
        if request.method == "POST" and cid:
            form = Payment_info_form(data=request.POST)
            if form.is_valid():
                payment_info = form.save()
                contact_info = Contact_info.objects.get(pk=cid)
                return redirect('checkout_review',
                                cid=contact_info.id,
                                pid=payment_info.id)
            else:
                messages.error(request, 'Invalid card information...')
                messages.error(request, form.errors)
        context = {
            'form': Payment_info_form(),
            'style': 'checkout.css',
            'script': 'checkout.js'
        }
        return render(request, 'cart/checkout_payment.html', context)
    else:
        raise Http404()

@login_required
def checkout_review(request, cid=None, pid=None):
    if request.user.customer.active_cart and cid and pid:
        contact_info = Contact_info.objects.get(pk=int(cid))
        payment_info = Payment_info.objects.get(pk=int(pid))
        if request.method == "POST" and contact_info and payment_info:
            if request.POST.get('create_order') == 'true':
                order = Order(
                    cart=request.user.customer.active_cart,
                    user=request.user,
                    contact=contact_info,
                    payment=payment_info,
                    status='Unpaid')
                order.save()
                return redirect('checkout_confirm',
                                oid=order.id)
        context = {
            'contact_info': contact_info,
            'payment_info': payment_info,
            'cart': request.user.customer.active_cart,
            'style': 'checkout.css'
        }
        return render(request, 'cart/checkout_review.html', context)
    else:
        raise Http404()

@login_required
def checkout_confirm(request, oid=None):
    if request.user.customer.active_cart and oid:
        order = Order.objects.get(pk=int(oid))
        if request.method == "POST":
            if request.POST.get('pay') == "pay" and order:
                order.status = "processing"
                order.save()
                order.user.customer.active_cart.status = "stale"
                order.user.customer.active_cart.save()
                order.user.customer.active_cart = None
                order.user.customer.save()
                messages.info(request, 'Payment successful.')
                messages.info(request, 'Your order is now processing.')
                return redirect('cart')
        context = {
            'order': order,
            'contact_info': order.contact,
            'cart': request.user.customer.active_cart,
            'style': 'checkout.css'
        }
        return render(request, 'cart/checkout_confirm.html', context)
    else:
        raise Http404()

