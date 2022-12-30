from django.contrib import admin

from .models import Product

# creamos la clase ProducAdmin para modificar el comportamiento
# de nuestro producto en el Administrador
class ProductAdmin(admin.ModelAdmin):
    # indicamos los campos a visualizar en el admin
    fields = ('title', 'description', 'price')
    # atributos que queremos mostrar del producto en admin
    list_display = ('__str__', 'slug', 'created_at')
    

# registramos nuestro modelo Produc en el Admin 
admin.site.register(Product, ProductAdmin)