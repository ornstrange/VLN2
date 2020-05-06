from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib.auth.hashers import make_password, check_password
from user.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = request.POST.copy()
        username = form.get("uname")
        password = make_password(form.get("pword"))
        cpassword = form.get("cpword")
        if check_password(cpassword, password):
            data = User(username=username, passhash=password, admin=0)
            data.save()
            return redirect('login')
        else:
            print("does not match") #TODO: inform the user
    return render(request, 'user/register.html')

