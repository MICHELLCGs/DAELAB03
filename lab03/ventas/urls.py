from django.urls import path
from . import views
app_name = 'ventas'
urlpatterns = [
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('ventas/', views.listar_ventas, name='listar_ventas'),
]

