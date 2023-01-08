from django.urls import path 
from . import views 

# indicar que las rutas siguientes le pertenecen a la app products
app_name = 'products'

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product') #id llave primaria, de esta form definimos ruta+slug= /slug de un producto
]


