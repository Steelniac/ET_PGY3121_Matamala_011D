function getAnimals() {
    const url = "https://api.petfinder.com/v2/animals?type=dog&location=90210";
    const headers = {
      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJOTXVDRVFUSEdjZlVTMmFmc2FlQmtyUGlhempjS3IyRjk0a2dyOVo0R28zUmdJcnBySiIsImp0aSI6IjY5NjU4N2M2OGZhZjI2MDAwMDA5NmJmYjNhMmM1MjA1ZjE4YTgwYmZiOTlmNmVlMDNiNmFiMmIyNzQ3MGE0NjYxMDg2MDFjZmJlMDM5MzUwIiwiaWF0IjoxNjg3Njc0NDI5LCJuYmYiOjE2ODc2NzQ0MjksImV4cCI6MTY4NzY3ODAyOSwic3ViIjoiIiwic2NvcGVzIjpbXX0.t9krHb1Vwc0_IADPzl35emFR-WhwCfB9f4xCOLJ01u1KDx8FEKAd23xlVklXf3D2eULSgLDxrLx6asIDP8JK84PLRJ78pw3uWAryGzHXEKnKfvNYZ0EhWeiPEI-a_POtPymwd70v8tHsZv8zxTRGLMjFtnioid8KjbJf-G4KZ6kppO1XnX0TZKnILc4Y8g6cGJZfB-0pusk8jrPThLUpDM6ZwTwd7GWQ1QRCMghDos3l0vGTZD_1S8CB9zB7i1pXdnNv7IjCKIPNBePQeFSwP15U2XuvQSe5Ssdk3dzphdctp49dn2LspbKu-YNtxlocm-MdCaKA2AxyncKwVFOTyQ",
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
        tableHeader.innerHTML = `
          <th>Nombre</th>
          <th>Especie</th>
          <th>Raza</th>
          <th>Edad</th>
          <th>Sexo</th>
          <th>Tamaño</th>
          <th>Descripción</th>
          <th>Foto</th>
        `;
        animalsTable.appendChild(tableHeader);
  
        data.animals.sort((a, b) => a.name.localeCompare(b.name)).forEach(animal => {
          const tableRow = document.createElement("tr");
          const photosHtml = animal.photos && animal.photos.length
            ? animal.photos.map(photo => `<img src="${photo.medium}" alt="Foto del animal"/>`).join("")
            : "";
          tableRow.innerHTML = `
            <td>${animal.name}</td>
            <td>${animal.species}</td>
            <td>${animal.breeds.primary}</td>
            <td>${animal.age}</td>
            <td>${animal.gender}</td>
            <td>${animal.size}</td>
            <td>${animal.description}</td>
            <td>${photosHtml}</td>
          `;
          animalsTable.appendChild(tableRow);
        });
      })
      .catch(error => console.error(error));
  }