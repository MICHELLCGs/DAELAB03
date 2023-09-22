from django.shortcuts import render
from .models import Proveedor, Cliente, Categoria, Producto, Venta, DetalleVenta

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ventas/listar_proveedores.html', {'proveedores': proveedores})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/listar_clientes.html', {'clientes': clientes})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'ventas/listar_categorias.html', {'categorias': categorias})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/listar_productos.html', {'productos': productos})

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})
