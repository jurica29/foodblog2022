# Importing forms from django
from django import forms
# Contact model imported from models
from .models import Contact

# Contact form used on the template about.html
class Contact(forms.ModelForm):
    class Meta:
        """Contact form"""
        model = Contact
        fields = ('fullname', 'message','email')
