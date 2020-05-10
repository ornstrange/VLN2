from django.shortcuts import render
from django.http import HttpResponse
from products import models as prod_models
from user import models as user_models
from . import models as cart_models

def index(request):
    return render(request, 'cart/index.html')

def checkout(request):
    return render(request, 'cart/checkout.html')

def add(request):
    if request.user.is_authenticated:
        id_ = request.POST.get('id')
        prod = prod_models.Product.objects.get(pk=id_)
        user = user_models.User_profile.objects.get(user=request.user)
        print(user)
        return HttpResponse("x")
    else:
        return HttpResponse("Not logged in")

