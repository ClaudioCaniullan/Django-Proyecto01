from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegistroForm



def index(request):
    return render(request, 'index.html',{
        'message':'Listado de productos', 
        'title':'Productos',
        'products': [
            {'title':'Playera', 'price':5, 'stock':True},
            {'title':'Camisa', 'price':7, 'stock':True},
            {'title':'Mochila', 'price':20, 'stock':False}
            ]
        }
    )


def loginview(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username') #POST es un diccionario
        password = request.POST.get('password')
        
        # el metodo authenticate busca en el DB username y password
        user= authenticate(username=username, password=password)

        if user:
            login(request,user)
            messages.success(request, 'bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario no valido')


    return render(request, 'users/login.html', )


def logoutview(request):
    logout(request)
    messages.success(request, 'sesion cerrada exitosamente')
    return redirect('loginview')


def registro(request):
    
    if request.user.is_authenticated:
        return redirect('index')
        
    form = RegistroForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
        
            
        
    return render(request,'users/registro.html', {
        'form':form
    })