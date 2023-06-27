from django.urls import path
from . import views
from .views import (
    index,
    quienes_somos,
    productos,
    adopta,
    test,
    mostrar_animales,
    producto_crear,
    mostrar,
    modificar,
    registrar,
    logout_view,
    CustomLoginView
    
)

urlpatterns = [
    path('', index, name='index'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('productos/', productos, name='productos'),
    path('adopta/', adopta, name='adopta'),
    path('test/', test, name='test'),
    path('mostrar_animales/', mostrar_animales, name='mostrar_animales'),
    path('producto/crear/', producto_crear, name='producto_crear'),
    path('mostrar/', mostrar, name="mostrar"),
    path('modificar/<int:id>/', views.modificar, name='modificar'),
    path('registrar/', registrar, name="registrar"),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]