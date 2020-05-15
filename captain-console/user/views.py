from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from user.forms import SignupForm, EditProfileForm
from user.models import User, Customer, Search
import os

def register(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.info(request, 'Registration successful!')
            messages.info(request, 'You can now login.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed!')
            messages.error(request, form.errors)
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
            goto = request.GET.get('next') or 'profile'
            return redirect(goto)
        else:
            messages.error(request, 'Login failed!')
            messages.error(request, form.errors)
    context = {
        'form': AuthenticationForm(),
        'style': 'user.css',
    }
    return render(request, 'user/login.html', context)

@login_required
def profile_view(request):
    context = {
        'style': 'user.css'
    }
    return render(request, "user/profile.html", context)

@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = EditProfileForm(request.POST, files=request.FILES, instance=user)
        alter_data = form.save(commit=False)
        if form.is_valid():
            customer = Customer.objects.get(user=user)
            if img := request.FILES.get('avatar'):
                try:
                    os.remove(os.path.join(settings.MEDIA_ROOT,
                                           customer.avatar.name))
                except:
                    pass
                customer.avatar = img
                customer.save()
            if not form.cleaned_data.get('first_name'):
                alter_data.first_name = User.objects.get(pk=user.id).first_name
            if not form.cleaned_data.get('last_name'):
                alter_data.last_name = User.objects.get(pk=user.id).last_name
            if not form.cleaned_data.get('email'):
                alter_data.email = User.objects.get(pk=user.id).email
            alter_data.save()
            messages.info(request, 'Your profile has been successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Changing profile information failed!')
            messages.error(request, form.errors)
    context = {
        'form': EditProfileForm(),
        'style': 'user.css'
    }
    return render(request, "user/edit.html", context)

@login_required
def searches(request):
    searches = Search.objects.filter(user=request.user.customer)
    context = {
        'searches': searches.order_by('-date'),
        'style': 'user.css'
    }
    return render(request, 'user/searches.html', context)

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.info(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Password change failed!')
            messages.error(request, form.errors)
    else:
        form = PasswordChangeForm(user=user)
    context = {
        'form': form
    }
    return render(request, "user/changepassword.html", context)

