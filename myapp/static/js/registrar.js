function validarRegistro() {
    // Obtener los datos ingresados por el registro
    var usuario = document.getElementById("usuario").value;
    var email = document.getElementById("email").value;
    var pass = document.getElementById("pass").value;
    var conf_pass = document.getElementById("conf_pass").value;
    var correoError = document.getElementById("correoError");

    // Limpiar mensajes de error
    correoError.textContent = "";

    // Validar campos vacíos
    if (usuario === "") {
        alert("Ingrese un usuario");
        return false;
    } else if (email === "") {
        alert("Ingrese un correo");
        return false;
    } else if (pass === "") {
        alert("Ingrese una contraseña");
        return false;
    } else if (conf_pass === "") {
        alert("Ingrese la confirmación de contraseña");
        return false;
    } else if (pass !== conf_pass) {
        alert("Las contraseñas no coinciden.");
        return false;
    }

    // Verificar si el correo ya está en uso mediante AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/verificar-correo/?email=' + encodeURIComponent(email), false);
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.correo_en_uso) {
                correoError.textContent = "Correo ya en uso";
                return false;
            }
        }
    };
    xhr.send();

    // Permitir el envío del formulario si no hay errores
    return true;
}
