from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
# import forms in view
from django import forms

# used to send message
from django.contrib import messages

# import contact model
from .models import Contact

# create a form from model contact
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('date_created', )

# Importing post model from models.py
from blogapp.models import Post

# I have used function based views below.
# Home page view - used to display only active posts and render home page
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'blog/frontpage.html', {'posts': posts})

# Contact page view 
def about(request):

    #
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'You have successfully submitted your message!')

    form = ContactForm

    context = {'form':form}


    return render(request, 'blog/about.html',context)

# Robots_txt is used for dealing with bots
def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

