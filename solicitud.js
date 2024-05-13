//Validar que los campos no esten vacios (sin informacion)

function validar(){
    
    //Obtengo los datos ingresados en los input

    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var rut = document.getElementById("rut").value;
    var correo = document.getElementById("correo").value;
    var numero = document.getElementById("numero").value;
    var servicio = document.getElementById("servicio").value;
    var descripcion = document.getElementById("descripcion").value;

    if (nombre == "") {
        alert('Ingrese un nombre')
    } else if (apellido == "") {
        alert('Ingrese un apellido')
    } else if (rut == "") {
        alert('Ingrese un rut')
    } else if (correo == "") {
        alert('Ingrese un correo electronico')
    } else if (numero == "") {
        alert('Ingrese un numero')
    } else if (servicio == "") {
        alert('Ingrese un servicio')
    } else if (descripcion == "") {
        alert('Ingrese una descripion')
    }

    
}

//Validar que inputs solo sean numeros

