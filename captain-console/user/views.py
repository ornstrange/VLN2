from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from user.forms import SignupForm, EditProfileForm
from user.models import User, Customer, Search
from django.contrib import messages

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
    return render(request, 'user/profile.html', context)

def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = EditProfileForm(request.POST,
                               files=request.FILES,
                               instance=request.user)
        if form.is_valid():
            customer = Customer.objects.get(user_id = user.id)
            if request.FILES['avatar']:
                customer.avatar = request.FILES['avatar']
                customer.save()
            form.save()
            return redirect('profile')
    context = {
        'form': EditProfileForm(),
        'style': 'user.css'
    }
    return render(request, 'user/edit.html', context)

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