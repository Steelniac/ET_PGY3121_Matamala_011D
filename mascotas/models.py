from django.db import models
from django.contrib.auth.models import User
import datetime

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
    codigo = models.CharField(primary_key=True, max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")
    cantidad = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='producto_imagenes', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
#boleta
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)

    