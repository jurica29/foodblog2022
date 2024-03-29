"""Used for routing URLs appropriately"""
from django.urls import path

from . import views


urlpatterns = [
    path("search/", views.search, name="search"),
    path("deleteComment/<str:pk>/", views.deleteComment, name="deleteComment"),
    path("editComment/<str:pk>/", views.editComment, name="editComment"),
    path("<slug:category_slug>/<slug:slug>/", views.detail, name="post_detail"),
    path("<slug:slug>/", views.category, name="category_detail"),
]
