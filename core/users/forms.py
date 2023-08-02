from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import User

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]