from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200, default='valor_predeterminado')
    photo = models.ImageField(upload_to='animal_photos')

    def __str__(self):
        return self.name
    
class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='producto_imagenes', null=True, blank=True)

    # Otros atributos que puedas necesitar

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_relacionado = models.ManyToManyField(Producto, through='ItemCarrito', related_name='carritos')

    def total(self):
        return sum(item.subtotal() for item in self.items.all())

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def subtotal(self):
        return self.producto.precio * self.cantidad

class Productost(models.Model):
    codigo = models.CharField(primary_key=True ,max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='producto_imagenes', null=True, blank=True)
    