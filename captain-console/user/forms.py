from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from user.models import Customer
<<<<<<< HEAD
from django.contrib.auth.forms import PasswordChangeForm
=======
<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.core.exceptions import ValidationError
>>>>>>> d6c8b509aeb4539980d59314e3043f935c262932
>>>>>>> dafa5b0a8b6682e6e437bc5b82b12f51bd2ecdf2

class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    first_name = forms.CharField(max_length=64,
                                 required=True,
                                 help_text='Required.')
    last_name = forms.CharField(max_length=64,
                                 required=False,
                                 help_text='Optional.')
    email = forms.EmailField(max_length=256,
                             required=True,
                             help_text='Required. Enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')



class EditProfileForm(UserChangeForm):
    avatar = forms.ImageField(required=False,
                              help_text="Optional.")
    password = None


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')                    
        exclude = ('password',)
        
