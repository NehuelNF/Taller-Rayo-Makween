fetch('https://randomuser.me/api/')
  .then(response => response.json())
  .then(data => {
    const trabajador1 = document.getElementById('trabajador1');
    trabajador1.src = data.results[0].picture.large;

    const nombre1 = document.getElementById('nombre1');
    nombre1.textContent = data.results[0].name.first + ' ' +data.results[0].name.last;
});

fetch('https://randomuser.me/api/')
    .then(response => response.json())
    .then(data => {
    const trabajador2 = document.getElementById('trabajador2');
    trabajador2.src = data.results[0].picture.large;

    const nombre2 = document.getElementById('nombre2');
    nombre2.textContent = data.results[0].name.first + ' ' +data.results[0].name.last;
      });


fetch('https://randomuser.me/api/')
.then(response => response.json())
.then(data => {
    const trabajador3 = document.getElementById('trabajador3');
    trabajador3.src = data.results[0].picture.large;

    const nombre2 = document.getElementById('nombre3');
    nombre2.textContent = data.results[0].name.first + ' ' +data.results[0].name.last;
});