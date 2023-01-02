
import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save



# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    # solo obtendremos productos atravez de su slug
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    
    # sobreescribimos el metodo para generar slug automaticos cons slugify
    #def __str__(self, *args, **kwargs):
    #   # generador de slug a partir del titulo del producto
    #   self.slug = slugify(self.title)
    #   super(Product, self).save(*args, **kwargs)
    
    # sobreescribimos este metodo para que que aparezca el producto con sus atributos
    def __str__(self):
        return self.title
    
# callbug que se encarga de generar nuevos slug
def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )
        
        instance.slug = slug
 
# registrar el callbug usando pre_save
# le indicamos a Django que cuando antes que un objeto product se 
# almacene debe ejecutar el callbug set_slug 
pre_save.connect(set_slug, sender=Product)
    
     