from django.urls import path
from . import views

urlpatterns = [
    path('login', views.sign_up, name='login'),
    path('register', views.register, name='register'),
]