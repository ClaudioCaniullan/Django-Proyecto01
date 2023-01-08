from django.contrib import admin

from .models import Category

# Register your models here.

# registramos nuestros modelos de '/categories/models.py'

admin.site.register(Category)