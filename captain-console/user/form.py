from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='uname', max_length=100)
    password = forms.CharField(label='pword',max_length=32, widget=forms.PasswordInput) 
    cpassword = forms.CharField(label='cpword',max_length=32, widget=forms.PasswordInput) 