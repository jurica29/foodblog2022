from django import forms
# Comement imported from models
from .models import Comment

# Used for comment option functionality/display
# Two fields, email and body which user can use


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')
