const postulacion = document.getElementById('postulacion');
const inputs = document.querySelectorAll('input');

const expresiones = {
    rut: /^[0-9]{7,8}-[0-9Kk]{1}$/,
    nombre: /^[a-zA-ZÀ-ÿ\s]{3,20}$/,
    appaterno: /^[a-zA-ZÀ-ÿ\s]{3,20}$/,
    apmaterno: /^[a-zA-ZÀ-ÿ\s]{3,20}$/,
    edad:/^(1[89]|[2-9][0-9]|35)$/,
    celular: /^ [0-9]{9,12}$/
}

const campos = {
    rut: false,
    nombre: false,
    appaterno: false,
    apmaterno: false,
    edad:false,
    celular:false
}

const validarPostulacion = (e) => {
    switch (e.target.name) {
        case "rut":
            validarCampo(expresiones.rut, e.target, 'rut');
            break;
        case "nombre":
            validarCampo(expresiones.nombre, e.target, "nombre");
            break;
        case "appaterno":
            validarCampo(expresiones.appaterno, e.target, "appaterno");
            break;
        case "apmaterno":
            validarCampo(expresiones.apmaterno, e.target, "apmaterno");
            break;
        case "edad":
            validarCampo(expresiones.edad, e.target, "edad");
        break;
        case "celular":
            validarCampo(expresiones.edad, e.target, "celular");
        break;
    }
}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`grupo_${campo}`).classList.remove('postulacion_grupo-incorrecto');
        document.getElementById(`grupo_${campo}`).classList.add('postulacion_grupo-correcto');
        document.querySelector(`#grupo_${campo} .postulacion_input-error`).classList.remove('postulacion_input-error-activo');
        campos[campo] = true;
    } else {
        document.getElementById(`grupo_${campo}`).classList.add('postulacion_grupo-incorrecto');
        document.getElementById(`grupo_${campo}`).classList.remove('postulacion_grupo-correcto');
        document.querySelector(`#grupo_${campo} .postulacion_input-error`).classList.add('postulacion_input-error-activo');
        campos[campo] = false;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarPostulacion);
    input.addEventListener("blur", validarPostulacion);
});

postulacion.addEventListener('submit', (e) => {
    e.preventDefault();

    const terminos = document.getElementById("terminos");
    if (campos.rut && campos.nombre && campos.appaterno && campos.apmaterno && campos.edad && campos.celular && terminos.checked) {
        postulacion.reset();
        document.getElementById('postulacion_mensaje-exito').classList.add('postulacion_mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('postulacion_mensaje-exito').classList.remove('postulacion_mensaje-exito-activo');
        }, 4000);
        document.querySelectorAll('.postulacion_grupo-correcto').forEach((icono) => {
            icono.classList.remove('postulacion_grupo-correcto');
        });
    } else {
        document.getElementById('postulacion_mensaje').classList.add('postulacion_mensaje-activo');
    }
});
