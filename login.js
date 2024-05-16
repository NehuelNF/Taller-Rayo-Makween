//Validamos que los campos no esten sin informacion

function validarLogin(){

    var usuario = document.getElementById("usuario").value;
    var pass = document.getElementById("pass").value;

    if (usuario == ""){
        alert('Ingrese su usuario o Correo electronico')
    } else if (pass == ""){
        alert('Ingrese su contraseña')
    } 

}