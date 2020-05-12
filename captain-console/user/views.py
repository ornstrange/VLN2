import os
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from user.models import User, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from . import forms

def register(request):
    if request.method == "POST":
        form = forms.SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    return render(request, "user/register.html", {
        "form": forms.SignupForm()
    })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    return render(request, "user/login.html", {
        "form": AuthenticationForm()
    })

def profile_view(request):
    return render(request, "user/profile.html")

def edit_profile(request):
    if request.method == "POST":
        print("ID: ", str(Customer.user_id))
        form = forms.EditProfileForm(request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            avatar = Customer.objects.get(user_id = User.id)
            avatar.avatar = request.FILES['avatar']
            avatar.save()
            form.save()
            return redirect('profile')
        else:
            print("Not valid")
    return render(request, "user/edit.html", {
        "form": forms.EditProfileForm()
    })

