from django import forms
# Comement imported from models
from .models import Comment

# Used for comment option functionality/display
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email','body')