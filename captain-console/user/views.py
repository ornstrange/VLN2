from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from user.models import User
from django.utils.crypto import get_random_string

# Create your views here.
def register(request):
    if request.method == 'POST':
        salt = get_random_string()
        data = request.POST.copy()
        # TODO: check if username exists - inform user
        username = data.get("uname")
        # TODO: add some password validators - inform user
        password = make_password(data.get("pword"), salt)
        cpassword = make_password(data.get("cpword"), salt)
        if password == cpassword:
            data = User(username=username, passhash=password, admin=0)
            data.save()
            return redirect('login')
        else:
            print("does not match") # TODO: inform the user
    return render(request, 'user/register.html')

