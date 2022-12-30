from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

# Crear vistas basadas en clases

class ProductListView(ListView):
    # template a utilizar
    template_name = 'index.html'
    # la consulta para obtener el listado de objetos
    queryset = Product.objects.all().order_by('-id')
    
    # sobre escribir el metodo get_context_data
    # este método pasa el contexto de la clase al template
    def get_context_data(self, **kwargs):
        # obtener el contexto de la clase padre
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de Productos'
        context['products'] = context['product_list']
        return context
    

# la clase DetailView se encargar de obtender un registro mediante un ID
class ProductDetailView(DetailView): #id == pk
    # indicar modelo con cual trabajar
    model = Product
    # especificar con el template a trabajar
    template_name = 'products/product.html'
    
    def get_context_data(self, **kwargs):
        # obtener el contexto de la clase padre
        context = super().get_context_data(**kwargs)
        # ver resultado en consola
        # print(context)

        return context