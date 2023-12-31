from django.db import models

class Proveedor(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    pagina_web = models.URLField()

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

class Cliente(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    direcciones = models.ManyToManyField(Direccion)
    telefonos = models.ManyToManyField('Telefono')

class Telefono(models.Model):
    numero = models.CharField(max_length=20)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Venta(models.Model):
    numero_factura = models.CharField(max_length=20, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_vendida = models.PositiveIntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

