import os
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from user.models import User, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from user.forms import SignupForm, EditProfileForm
from user.models import User, Customer, Search
from django.contrib import messages

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
        else:
            messages.error(request, f"Please enter both passwords correctly")
    context = {
        'form': SignupForm(),
        'style': 'user.css'
    }
    return render(request, 'user/register.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, f"Login failed!")
            messages.error(request, f"Please enter username and password correctly")
    context = {
        'form': AuthenticationForm(),
        'style': 'user.css',
    }
    return render(request, 'user/login.html', context)

def profile_view(request):
    return render(request, "user/profile.html")

def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = forms.EditProfileForm(request.POST, files=request.FILES, instance=request.user)
        alter_data = form.save(commit=False)
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        if form.is_valid():
            avatar = Customer.objects.get(user_id = user.id)
            if request.FILES:
                try:
                    os.remove("media/"+str(avatar.avatar))
                except:
                    pass
                try:
                    avatar.avatar = request.FILES['avatar']
                    avatar.save()
                except:
                    pass
            if form.cleaned_data.get('first_name') == "":
                alter_data.first_name = User.objects.get(id = user.id).first_name
            if form.cleaned_data.get('last_name') == "":
                alter_data.last_name = User.objects.get(id = user.id).last_name
            if form.cleaned_data.get('email') == "":
                alter_data.email = User.objects.get(id = user.id).email
            alter_data.save()
            return redirect('profile')
        else:
            print("Not valid")
    return render(request, "user/edit.html", {
        "form": forms.EditProfileForm()
    })
def searches(request):
    searches = Search.objects.filter(user=request.user.customer)
    context = {
        'searches': searches.order_by('-date'),
        'style': 'user.css'
    }
    return render(request, 'user/searches.html', context)

def forgotten_view(request):
    
    context = {
        'style': 'user.css'
    }
    return render(request, 'user/forgotten.html', context)