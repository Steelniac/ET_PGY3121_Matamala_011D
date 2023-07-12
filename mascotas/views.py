
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import ProductoForm,RegistroUserForm
from .models import *
from mascotas.compra import Carrito


def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def adopta(request):
    return render(request, 'adopta.html')

def sinresgistro(request):
    return render(request, 'sinregistro.html')

def test(request):
    return render(request, 'test.html')

def mostrar_animales(request):
    url = "https://api.petfinder.com/v2/animals?type=dog&location=90210"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJOTXVDRVFUSEdjZlVTMmFmc2FlQmtyUGlhempjS3IyRjk0a2dyOVo0R28zUmdJcnBySiIsImp0aSI6ImEzZTM4MTQ5OWFiZTg1ZTdmNTVjMDEyNDFlZjY4ZmRlODYwN2E0NGI4YzVmYTI2ZTFhZWMwMDljZTU0YmVlMjlmOTIwNzcxNzQ2YjY0OGRhIiwiaWF0IjoxNjg3Njc3MDM3LCJuYmYiOjE2ODc2NzcwMzcsImV4cCI6MTY4NzY4MDYzNywic3ViIjoiIiwic2NvcGVzIjpbXX0.Y8o6EAsGKrdAUn6zooynMsB0LZX8OTOPHF8XauJJfAe0ndf2tFpP-rOWCp3YPSQzTL8KNkM2GAFCcc-cC3i5xpsVJ0sWpB7gs99UQhm8EUHK6R1GPrtVr-eNMJE58pJUB1iC6iiMhah-tQh-RyNk7AZQUk7Kp_2QfxFaUHHXtCY0b6-d_z16C25cqNdGiVdtcevFr558bWsVK_ciLAPgK5WuTDkefoD7xvLzazzamp_uOqzNfhO3fWMTA88lRqf8IfFeDVKo6MlXRAS3f7iIBjpwzFyxFbbqJrbpX2OAhghGUf0IfL4xO8kY0c4ILhMUTOLQq5PxiJdlj8Bq2NUYjQ",
        "Content-Type": "application/json"
    }

    response = request.get(url, headers=headers)
    animals = response.json().get("animals", [])

    return render(request, "mostrar_animales.html", {"animals": animals})

def registrar(request):
    data = {
        'form' : RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                                password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def logout_view(request):
    return render(request, 'index.html')


class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/'
    
def donaciones_view(request):
    return render(request, 'donaciones.html')





#CRUD PRODUCTO


def mostrarPro(request):
    #obtenemos todos los vehiculos almacenados en la clase
    producto = Producto.objects.all()
    #creamos un diccionario
    datos={
        'productos':producto
    }
    #devolvemos a un template el diccionario y su contenido
    return render(request, 'mostrarproducto.html', datos)
#Producto
def eliminarPro(request, id):
    producto = Producto.objects.get(codigo=id)
    producto.delete()
    return redirect('mostrarProducto')


def crearPro(request):
    if request.method=='POST': 
        productoForm = ProductoForm(request.POST,request.FILES)
        if productoForm.is_valid():
            productoForm.save()     #similar al insert
            return redirect('mostrarProducto')
    else:
        productoForm=ProductoForm()
    return render(request, 'crearproducto.html', {'productoForm':productoForm})


def modificarPro(request, id):
    producto = Producto.objects.get(codigo=id) #buscamos el objeto x patente = id
    datos ={
        'form': ProductoForm(instance=producto) #instanciamos el obj. en un obj. de tipo formulario
    }
    #el siguiente bloque modifica el contenido del objeto almacenado
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrarProducto')
    
    return render(request, 'modificarproducto.html', datos)

#tienda

def tienda(request):
    producto = Producto.objects.all()
    datos={
        'productos':producto
    }
    return render(request, 'tienda.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.agregar(producto=producto)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    productos = Producto.objects.get(codigo=id)
    carrito_compra.eliminar(productos=productos)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    productos = Producto.objects.get(patente=id)
    carrito_compra.restar(productos=productos)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(codigo = value['codigo'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)
