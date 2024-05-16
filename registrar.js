//Validar que los campos no esten vacios (sin informacion)
function validarResgistro(){

    //Obtenermos los datos ingresados por el registro

    var usuario = document.getElementById("usuario").value;
    var email = document.getElementById("email").value;
    var pass = document.getElementById("pass").value;
    var conf_pass = document.getElementById("conf_pass").value;

    if (usuario == ""){
        alert('Ingrese un usuario')
    } else if (email == ""){
        alert('Ingrese un correo')
    } else if (pass == ""){
        alert ('Ingrese una contraseña')
    } else if (conf_pass == ""){
        alert ('Ingrese la confirmacion de contraseña')
    }


}

