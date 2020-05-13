from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from user.models import User, Customer
from user.forms import SignupForm, EditProfileForm

def register(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
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
    context = {
        'form': AuthenticationForm(),
        'style': 'user.css',
    }
    return render(request, 'user/login.html', context)

def profile_view(request):
    context = {
        'style': 'user.css'
    }
    return render(request, 'user/profile.html', context)

def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = EditProfileForm(request.POST,
                               files=request.FILES,
                               instance=request.user)
        if form.is_valid():
            avatar = Customer.objects.get(user_id = user.id)
            avatar.avatar = request.FILES['avatar']
            avatar.save()
            form.save()
            return redirect('profile')
    context = {
        'form': EditProfileForm(),
        'style': 'user.css'
    }
    return render(request, 'user/edit.html', context)

