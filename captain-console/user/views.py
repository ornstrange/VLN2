from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from user.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "user/register.html", {
        "form": UserCreationForm()
    })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm()
    
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html",{"form":form})

