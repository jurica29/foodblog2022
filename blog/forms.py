"""Importing forms"""
from django import forms

from .models import Contact


class Contact(forms.ModelForm):
    """Contact form"""

    class Meta:
        """Inner class"""

        model = Contact
        fields = ("fullname", "message", "email")
