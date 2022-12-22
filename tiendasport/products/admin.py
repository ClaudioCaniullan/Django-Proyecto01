from django.contrib import admin

from .models import Product

# registramos nuestro modelo Produc en el Admin 
admin.site.register(Product)