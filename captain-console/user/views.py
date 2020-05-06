from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import UserCreationForm

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
    

