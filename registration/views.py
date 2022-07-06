from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/frontpage')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})

def sign_up(request):
    return render(request, 'registration/login.html', {})