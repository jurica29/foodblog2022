from django.shortcuts import redirect, render, reverse
from .forms import RegisterForm
# Importing login,logout and authentication systems for this app
from django.contrib.auth import login, logout, authenticate

# Function based views used
#  View for register page
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('frontpage'))
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})

# View for login page
def sign_up(request):
    return render(request, 'registration/login.html', {})

# View for log out page
def log_out(request):
    logout(request)
    return render(request, 'registration/logout.html', {})
    