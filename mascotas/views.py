import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import ProductoForm,RegistroUserForm
from .models import Producto

def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def adopta(request):
    return render(request, 'adopta.html')

def test(request):
    return render(request, 'test.html')

def mostrar_animales(request):
    url = "https://api.petfinder.com/v2/animals?type=dog&location=90210"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJOTXVDRVFUSEdjZlVTMmFmc2FlQmtyUGlhempjS3IyRjk0a2dyOVo0R28zUmdJcnBySiIsImp0aSI6ImEzZTM4MTQ5OWFiZTg1ZTdmNTVjMDEyNDFlZjY4ZmRlODYwN2E0NGI4YzVmYTI2ZTFhZWMwMDljZTU0YmVlMjlmOTIwNzcxNzQ2YjY0OGRhIiwiaWF0IjoxNjg3Njc3MDM3LCJuYmYiOjE2ODc2NzcwMzcsImV4cCI6MTY4NzY4MDYzNywic3ViIjoiIiwic2NvcGVzIjpbXX0.Y8o6EAsGKrdAUn6zooynMsB0LZX8OTOPHF8XauJJfAe0ndf2tFpP-rOWCp3YPSQzTL8KNkM2GAFCcc-cC3i5xpsVJ0sWpB7gs99UQhm8EUHK6R1GPrtVr-eNMJE58pJUB1iC6iiMhah-tQh-RyNk7AZQUk7Kp_2QfxFaUHHXtCY0b6-d_z16C25cqNdGiVdtcevFr558bWsVK_ciLAPgK5WuTDkefoD7xvLzazzamp_uOqzNfhO3fWMTA88lRqf8IfFeDVKo6MlXRAS3f7iIBjpwzFyxFbbqJrbpX2OAhghGUf0IfL4xO8kY0c4ILhMUTOLQq5PxiJdlj8Bq2NUYjQ",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    animals = response.json().get("animals", [])

    return render(request, "mostrar_animales.html", {"animals": animals})

def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    
    return render(request, 'producto_crear.html', {'form': form})



def mostrar(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'mostrar.html', datos)

def modificar(request, id):
    productoModificado = Producto.objects.get(id=id)  # buscamos el objeto
    datos = {
        'form': ProductoForm(instance=productoModificado)
    }
    if request.method == "POST":
        formulario = ProductoForm(request.POST, request.FILES, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('otra')
    return render(request, 'modificar.html', datos)

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