function validarCarro(){

    var calles = document.getElementById("calles").value;
    var numeros = document.getElementById("numeros").value;
    var correo = document.getElementById("correo").value;
    var contacto = document.getElementById("contacto").value;
    var servicio = document.getElementById("Servicio").value;
    var indicaciones = document.getElementById("indicaciones").value;

    if (calles == ""){
        alert('Ingrese la calle')
    } else if (numeros == ""){
        alert('Ingrese el numero')
    } else if (correo == ""){
        alert ('Ingrese el correo')
    } else if (contacto == ""){
        alert ('Ingrese un contacto')
    } else if (servicio == "") {
        alert ('Ingrese un servicio')
    } else if (indicaciones == ""){
        alert('Ingrese las indicaciones')
    } else {
        confirm('¿Está seguro de la información otorgada?')
    }


}