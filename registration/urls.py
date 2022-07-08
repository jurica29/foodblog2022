from django.urls import path
from . import views

# URL configuration for register app including all pages that it has
urlpatterns = [
    path('login', views.sign_up, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.log_out, name='log_user_out'),
]