"""Importing models from database"""
from django import forms

# Comement imported from models
from .models import Comment

# Used for comment option functionality/display
# Two fields, email and body which user can use


class CommentForm(forms.ModelForm):
    """Class used for comment form"""

    class Meta:
        """Inner class"""

        model = Comment
        fields = ("email", "body")
        # Fixing the size of comment box
        widgets = {
            "body": forms.Textarea(attrs={"rows": 10, "cols": 30}),
        }
