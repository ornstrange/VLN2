from django.shortcuts import render

def index(request):
    return render(request, 'cart/index.html')

def checkout(request):
    return render(request, 'cart/checkout.html')

