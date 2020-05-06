from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from user.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get("uname") #TODO: check if username exists - inform user
        password = make_password(data.get("pword")) #TODO: add some password validators - inform user
        cpassword = data.get("cpword")
        if check_password(cpassword, password):
            data = User(username=username, passhash=password, admin=0)
            data.save()
            return redirect('login')
        else:
            print("does not match") #TODO: inform the user
    return render(request, 'user/register.html')

