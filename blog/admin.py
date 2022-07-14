from django.contrib import admin

# Registered admin models
from .models import Contact

admin.site.register(Contact)
