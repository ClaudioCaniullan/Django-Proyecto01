from django.urls import path 
from . import views 

urlpatterns = [
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product') #id llave primaria, de esta form definimos ruta+slug= /slug de un producto
    
]


