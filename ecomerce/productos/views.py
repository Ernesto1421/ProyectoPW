from django.shortcuts import render

# Create your views here.
from .models import Producto
def home(request):
    productos = Producto.objects.all()
    context ={'productos': productos}
    template = 'productos/home.html'
    

    return render (request, template, context)

def todos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    template = 'productos/all.html'
    return render(request, template, context)

        
