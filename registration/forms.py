"""Importing forms"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """Registration form"""
    email = forms.EmailField(required=True)

    class Meta:
        """Using below fields for the form"""
        model = User
        fields = ["username", "email", "password1", "password2"]
