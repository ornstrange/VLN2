import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from user.forms import SignupForm, EditProfileForm
from user.models import User, Customer, Search
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
    context = {
        'style': 'user.css'
    }
    return render(request, "user/profile.html", context)

def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = forms.EditProfileForm(request.POST, files=request.FILES, instance=request.user)
        alter_data = form.save(commit=False)
        if form.is_valid():
            customer = Customer.objects.get(user=user)
            if request.FILES.get('avatar'):
                try:
                    os.remove(os.path.join(settings.MEDIA_ROOT, customer.avatar.name))
                except:
                    pass
                customer.avatar = request.FILES.get('avatar')
                customer.save()
            if form.cleaned_data.get('first_name') == "":
                alter_data.first_name = User.objects.get(id = user.id).first_name
            if form.cleaned_data.get('last_name') == "":
                alter_data.last_name = User.objects.get(id = user.id).last_name
            if form.cleaned_data.get('email') == "":
                alter_data.email = User.objects.get(id = user.id).email
            alter_data.save()
            return redirect('profile')
        else:
            messages.error(request, f"{form.errors}")
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


def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  
            messages.success(request, f'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, f'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
    return render(request, "user/changepassword.html", {
        "form": forms.PasswordChangeForm(data=request.POST, user=request.user)
    })