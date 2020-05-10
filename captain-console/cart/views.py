from django.shortcuts import render, redirect
from products.models import Product
from user.models import Customer
from cart.models import Cart

def index(request):
    return render(request, 'cart/index.html')

def checkout(request):
    return render(request, 'cart/checkout.html')

def add(request):
    if request.user.is_authenticated:
        prod_id = request.POST.get('id')
        prod = Product.objects.get(pk=prod_id)
        print(Customer.objects.all())
        print(request.user.pk)
        return redirect('product', prod.id)
    else:
        return redirect('product', prod.id)

