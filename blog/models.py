"""Importing models from django database"""
from django.db import models


class Contact(models.Model):
    """Custom model for contact form with customised fields below"""
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    date_created = models.DateField(
        verbose_name="Created on date",
        auto_now_add="True")

    def __str__(self):
        """Returns email contact names within django admin area"""
        return self.email
