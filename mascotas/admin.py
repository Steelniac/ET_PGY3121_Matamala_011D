from django.contrib import admin
from .models import Animal
from .models import Producto,Boleta,detalle_boleta

# Register your models here.
admin.site.register(Animal)
admin.site.register(Producto)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)
