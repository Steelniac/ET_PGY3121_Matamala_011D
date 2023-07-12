from django.urls import path
from . import views 

from .views import (
    index,
    quienes_somos,
    productos,
    adopta,
    mostrar_animales,
    registrar,
    logout_view,
    CustomLoginView,
    mostrarPro,
    modificarPro,
    crearPro,
    eliminarPro,
    generarBoleta,
    agregar_producto,
    eliminar_producto,
    restar_producto,
    limpiar_carrito,tienda
    
)

urlpatterns = [
    path('', index, name='index'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('productos/', productos, name='productos'),
    path('adopta/', adopta, name='adopta'),
    path('mostrar_animales/', mostrar_animales, name='mostrar_animales'),
    path('registrar/', registrar, name="registrar"),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('donaciones/', views.donaciones_view, name='donaciones'),
    path('mostrarproducto/',mostrarPro, name='mostrarProducto'),
    path('modificarproducto/<id>',modificarPro,name='modificarproducto'),
    path('crearproducto/',crearPro,name='crearproducto'),
    path('eliminarproducto/<id>',eliminarPro,name='eliminarproducto'),
    

    path('tienda/',tienda, name="tienda"),
   
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),

    
]