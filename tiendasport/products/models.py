from django.db import models
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    # solo obtendremos productos atravez de su slug
    slug = models.SlugField(null=False, blank=False, unique=True)
    
    # sobreescribimos el metodo para generar slug automaticos
    def __str__(self, *args, **kwargs):
        # generador de slug a partir del titulo del producto
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
    
    # sobreescribimos este metodo para que que aparezca el producto con sus atributos
    def __str__(self):
        return self.title
    
