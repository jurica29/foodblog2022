from django.db import models

# Custom model for contact form page consisting of below fields
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000) 
    date_created = models.DateField(verbose_name="Created on date", auto_now_add="True")

# Displaying email contact names within django admin section
    def __str__(self):
        return self.email