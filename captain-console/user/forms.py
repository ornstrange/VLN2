from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from user.models import Customer
from django.contrib.auth.forms import PasswordChangeForm

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

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

