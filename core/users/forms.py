from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            self.add_error("username", "Username already exists.")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            self.add_error("email", "Email already exists.")

        return cleaned_data
