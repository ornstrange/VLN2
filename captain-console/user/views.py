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
                except FileNotFoundError:
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
    customer = request.user.customer
    searches = Search.objects.filter(customer=customer)
    context = {
        'searches': searches,
        'style': 'user.css'
    }
    return render(request, 'user/searches.html', context)

