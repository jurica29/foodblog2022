"""Provides an inbound HTTP request to a Django web application."""
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django import forms


from django.contrib import messages


from blogapp.models import Post


from .models import Contact


class ContactForm(forms.ModelForm):
    """Contact form view"""
    class Meta:
        """The inner class of the model class"""
        model = Contact
        exclude = ('date_created', )


def frontpage(request):
    """Home page view"""
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'blog/frontpage.html', {'posts': posts})


def about(request):
    """Contact page view """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(
                request, 'You have successfully submitted your message!')

    form = ContactForm

    context = {'form': form}

    return render(request, 'blog/about.html', context)


def robots_txt(request):
    """Robots_txt is used for dealing with bots"""
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
