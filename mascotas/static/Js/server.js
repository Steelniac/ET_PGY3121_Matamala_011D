const express = require('express');
const fetch = require('node-fetch');
const app = express();
const port = 3000;

app.get('/animals', (req, res) => {
  const url = "https://api.petfinder.com/v2/animals?type=dog&location=90210";
  const headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJOTXVDRVFUSEdjZlVTMmFmc2FlQmtyUGlhempjS3IyRjk0a2dyOVo0R28zUmdJcnBySiIsImp0aSI6ImEzZTM4MTQ5OWFiZTg1ZTdmNTVjMDEyNDFlZjY4ZmRlODYwN2E0NGI4YzVmYTI2ZTFhZWMwMDljZTU0YmVlMjlmOTIwNzcxNzQ2YjY0OGRhIiwiaWF0IjoxNjg3Njc3MDM3LCJuYmYiOjE2ODc2NzcwMzcsImV4cCI6MTY4NzY4MDYzNywic3ViIjoiIiwic2NvcGVzIjpbXX0.Y8o6EAsGKrdAUn6zooynMsB0LZX8OTOPHF8XauJJfAe0ndf2tFpP-rOWCp3YPSQzTL8KNkM2GAFCcc-cC3i5xpsVJ0sWpB7gs99UQhm8EUHK6R1GPrtVr-eNMJE58pJUB1iC6iiMhah-tQh-RyNk7AZQUk7Kp_2QfxFaUHHXtCY0b6-d_z16C25cqNdGiVdtcevFr558bWsVK_ciLAPgK5WuTDkefoD7xvLzazzamp_uOqzNfhO3fWMTA88lRqf8IfFeDVKo6MlXRAS3f7iIBjpwzFyxFbbqJrbpX2OAhghGUf0IfL4xO8kY0c4ILhMUTOLQq5PxiJdlj8Bq2NUYjQ",
    "Content-Type": "application/json"
  };

  fetch(url, {
    headers: headers
  })
    .then(response => response.json())
    .then(data => {
      res.json(data);
    })
    .catch(error => {
      console.error(error);
      res.status(500).json({ error: 'Error al obtener los animales' });
    });
});

app.listen(port, () => {
  console.log(`Servidor escuchando en el puerto ${port}`);
});