"""Importing redirect, render and reverse"""
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, reverse
from .forms import RegisterForm


def register(request):
    """View for register page"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('frontpage'))
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})


def sign_up(request):
    """View for login page"""
    return render(request, 'registration/login.html', {})


def log_out(request):
    """View for log out page"""
    logout(request)
    return render(request, 'registration/logout.html', {})
