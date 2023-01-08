from django.db import models

# importar modelo Product desde la app products para
# generar relacion manytomany

from products.models import Product

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # Generar una relacion manytomany entre as clases Categry/Product
    products = models.ManyToManyField(Product, blank=True)
    # registramos el momento cuando fue creado un elemento
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title