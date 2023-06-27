$(function() {
            
    $("#mi-Formulario").validate({
        rules: {
            
            email: {
                required: true,
                email: true
            },
            fono: {
                required: true,
                number: true,
                minlength: 9
            },
            cupon:{
                required: false
            },
            
        },
        messages: {
            
            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            fono: {
                required: 'Ingrese un número de celular',
                minlength: 'Cantidad de dígitos insuficiente (mínimo 9)'
            },
                        
            
        }
    });
});

// Definimos una función para validar el cupón
function validarCupon() {
    // Obtenemos el valor del cupón ingresado por el usuario
    var cupon = document.getElementById("cupon").value;
  
    // Creamos un array con los cupones disponibles
    var cuponesDisponibles = ["Masco2023", "DescuentoPet", "OfertaFurry"];
  
    // Validamos si el cupón ingresado por el usuario está en el array de cupones disponibles
    if (cuponesDisponibles.includes(cupon)) {
      // Si el cupón es válido, mostramos un mensaje de éxito
      alert("Cupón aplicado correctamente");
    } else {
      // Si el cupón no es válido, mostramos un mensaje de error
      alert("Cupón inválido o no disponible");
    }
  }
  
  // Definimos una función para calcular el total de la compra
function calcularTotal() {
    // Obtenemos los valores seleccionados por el usuario
    var producto = document.getElementById("seleccion-producto").value;
    var cantidad = document.getElementById("cantidad-producto").value;
  
    // Calculamos el total de la compra
    var total = 10990 * cantidad;
  
    // Mostramos el total en un mensaje de alerta
    alert("El total de la compra es: $" + total);
}

function validarCampos() {
  // Obtenemos los valores ingresados por el usuario
  var cupon = document.getElementById("cupon").value;
  var producto = document.getElementById("seleccion-producto").value;
  var cantidad = document.getElementById("cantidad-producto").value;

  // Verificamos si los campos requeridos tienen datos
  if (!cupon && !producto && !cantidad) {
    // Si los campos están vacíos, mostramos un mensaje de error
    alert("Debe ingresar un cupón y seleccionar un producto y una cantidad");
  } else if (!cupon) {
    // Si el cupón está vacío, mostramos un mensaje de error
    alert("Debe ingresar los datos para segir");
  } else if (!producto || !cantidad) {
    // Si el producto o la cantidad están vacíos, mostramos un mensaje de error
    alert("Debe seleccionar un producto y una cantidad");
  } else {
    // Si todos los campos tienen datos, ejecutamos las funciones
    validarCupon();
    calcularTotal();
  }
}

function colorOrange(obj){
  obj.style.backgroundColor='#A2CDE6';
}

function colorBlanco(obj){
  obj.style.backgroundColor='white';
}

function upperText(texto)
{
  const x = texto;
  x.value= x.value.toUpperCase();
}


function getAnimals() {
    const url = "https://api.petfinder.com/v2/animals?type=dog&location=90210";
    const headers = {
      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJOTXVDRVFUSEdjZlVTMmFmc2FlQmtyUGlhempjS3IyRjk0a2dyOVo0R28zUmdJcnBySiIsImp0aSI6IjdkNjc4YzVjYTgwY2ExNTg1MmU4ZjFkMDZiNGVlNGNhODA0NWIwYTU0MTVjOGIwYzMxZjI1NzEzMmNiMDU1ZjRjMmRjNDgzOTRiMjc3Y2FlIiwiaWF0IjoxNjg3NjczMTc1LCJuYmYiOjE2ODc2NzMxNzUsImV4cCI6MTY4NzY3Njc3NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.bB1QvsAyKO2sSb9V0ZWAVHTPUbrjCExVGvdM2jOWcnQsHHWeCdIUU0Fb11c4C-cRGbMbIcyHF3uAUjzT9BTnXHgccImsEMadqiQJzBKSz6ILXejhDCCtRUfwcwvCPaf6_Bi6tZGuBwE3HiNQzsHrtxW1lVAxbOegRwlVLcLUsIRwQncE1ipZaBnTsd8-DpuwPnIn6UrwoFOFfldP-inugsUhAuOokCXA1kg-0mCt4tI4lgw8wU57soWJTffyzUpEvAQq5_oU-wBgMI4A-_tvmrkGTHcqVX7vSa3yMdsEe1_7BC7mmqd6f9tZBn6auQ_4JkNBNcbBNC0MuKq76pUy1g",
      "Content-Type": "application/json"
    };
    fetch(url, {
      headers: headers
    })
    .then(response => response.json())
    .then(data => {
      const animalsTable = document.getElementById("animals");
      animalsTable.innerHTML = "";
      const tableHeader = document.createElement("tr");
      tableHeader.innerHTML = "<th>Nombre</th><th>Especie</th><th>Raza</th><th>Edad</th><th>Sexo</th><th>Tamaño</th><th>Descripcion</th><th>foto</th>";
      animalsTable.appendChild(tableHeader);
      data.animals.sort((a, b) => (a.name > b.name) ? 1 : -1).forEach(animal => {
        const tableRow = document.createElement("tr");
        let photosHtml = "";
        if (animal.photos && animal.photos.length) {
          photosHtml = animal.photos.map(photo => `<img src="${photo.medium}"/>`).join("");
        }
        tableRow.innerHTML = `<td>${animal.name}</td><td>${animal.species}</td><td>${animal.breeds.primary}</td><td>${animal.age}</td><td>${animal.gender}</td><td>${animal.size}</td><td>${animal.description}</td><td>${photosHtml}</td>`;
        animalsTable.appendChild(tableRow);
      });
    })
    .catch(error => console.error(error));
  }