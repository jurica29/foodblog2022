"""Importing render"""
from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "blog/not_found.html")


def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "blog/not_found.html")
