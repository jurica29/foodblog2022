from django.urls import path

from . import views

# URL configuration for search bar, detail page and category detail
urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'), 
    path('<slug:slug>/', views.category, name='category_detail')
] 
