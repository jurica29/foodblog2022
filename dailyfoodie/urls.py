"""dailyfoodie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Main URL configuration of the project
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include
from blog.views import frontpage, about, robots_txt
from .sitemaps import CategorySitemap, PostSitemap

# Sitemaps is used to provide information about everything on the website
sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

# Urls of all apps used for this website
urlpatterns = [
    # Url for sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    # Url for robots.txt
    path('robots.txt', robots_txt, name='robots_txt'),
    # Urls for admin area
    path('admin/', admin.site.urls),
    # Url for contact page
    path('about/', about, name='about'),
    # Url for registration app urls
    path('registration/', include('registration.urls')),
    # Url for blogapp urls
    path('blogapp/', include('blogapp.urls')),
    # Url for authorization
    path('', include("django.contrib.auth.urls")),
    # Url for home page
    path('', frontpage, name='frontpage'),
] 
