from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from user.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

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
    if request.method == "GET":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")

    return render(request, "user/index.html", {
        "form": AuthenticationForm()
    })

