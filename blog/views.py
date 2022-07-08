from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Importing post model from models.py
from blogapp.models import Post

# I have used function based views below.
# Home page view - used to display only active posts and render home page
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'blog/frontpage.html', {'posts': posts})

# About page view - renders about page
def about(request):
    return render(request, 'blog/about.html')

# Robots_txt is used for dealing with bots
def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")