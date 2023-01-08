from django.shortcuts import render

# esta clase nos permite ejecutar consultas aplicando diferentes filtros
from django.db.models import Q 

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
    
    
class ProductSearchListView(ListView):
    template_name = 'products/search.html'
    
    # sobreescribir el metodo get_queryset para retornar queryset
    def get_queryset(self):
        # buscaremos elementos tanto por titulo o por su categoria
        filters = Q(title__icontains = self.query()) | Q(category__title__icontains=self.query())
        # SELECT * FROM products WHERE title like %valor%
        return Product.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')
    
    
    # sobre escribir el metodo get_context_data
    # este método pasa el contexto de la clase al template
    def get_context_data(self, **kwargs):
        # obtener el contexto de la clase padre
        context = super().get_context_data(**kwargs)
        context['products'] = context['product_list']
        context["query"] = self.query()
        context['count'] = context['product_list'].count()
        return context
    