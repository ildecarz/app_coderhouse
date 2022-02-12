from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Cuenta

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:

        model  = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ['username', 'email']


class CuentaUpdateForm(forms.ModelForm):
    
    class Meta:

        model = Cuenta
        fields = ['imagen']