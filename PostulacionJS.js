function formulario(){
    console.log('Enviar');

    var rut = document.getElementById('rut');
    var nombre = document.getElementById('nombre');
    var apaterno = document.getElementById('apaterno');
    var amaterno = document.getElementById('amaterno');
    var edad = document.getElementById('edad');
    var celular = document.getElementById('celular');
    var error1 = document.getElementById("error1");
    var error2 = document.getElementById("error2");
    var error3 = document.getElementById("error3");
    var error4 = document.getElementById("error4");
    var error5 = document.getElementById("error5");
    var error6 = document.getElementById("error6");

    var mensajeError=[];

    if (nombre.value.length<3  || nombre.value.length>20){
        mensajeError.push('Ingrese un nombre con mas de 3 caracteres y menos de 20')
        error1.innerHTML=mensajeError.join(',');
    }
    if (rut.value.length<9 || rut.value.length>10){
        mensajeError.push('Ingrese un rut valido');
        error2.innerHTML=mensajeError.join(',');
    }
    if (apaterno.value.length<3 || apaterno.value.length>20){
        mensajeError.push("Ingrese un apellido con mas de 3 caracteres y menos de 20")
        error3.innerHTML=mensajeError.join(',');
    }
    if (amaterno.value.length<3 || amaterno.value.length >20){
        mensajeError.push("Ingrese un apellido con mas de 3 caracteres y menos de 20")
        error4.innerHTML=mensajeError.join(',');
    }
    if (edad.value.length<18 || edad.value.length>35){
        mensajeError.push("Su edad tiene que ser mayor a 18 y menor a 35")
        error5.innerHTML=mensajeError.join(',');
    }

    if (celular.value.length<9 || celular.value.length>12){
        mensajeError.push("El numero debe tener un largo entre 9 y 12 numeros")
        error6.innerHTML=mensajeError.join(',');
    }

    return false;
}