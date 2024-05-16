document.addEventListener("DOMContentLoaded", function() {

    const popoverButton = document.querySelector(".btnn");

    var popover = new bootstrap.Popover(popoverButton, {
        title: 'Carrito de compra',
        content: "¡ El carrito no esta disponible de momento !",
        trigger: "hover",
        container: 'body'
    });

    popoverButton.addEventListener('click', function () {
        popover.toggle();
    });
})

//API DE HORA SANTIAGO
$(function() {
    // Función para obtener la hora actual de Santiago
    function obtenerHoraSantiago() {
        // Hacer la solicitud GET a la API de World Time para obtener la hora de Santiago
        $.get("http://worldtimeapi.org/api/timezone/America/Santiago", function(data) {
            var horaSantiago = new Date(data.utc_datetime); 
            verificarHorario(horaSantiago);
        });
    }

    // Función para verificar si el taller está abierto o cerrado
    function verificarHorario(horaSantiago) {
        var hora = horaSantiago.getHours();
        
        // Verificar si la hora está entre las 7:00 AM y las 7:00 PM
        if (hora >= 7 && hora < 19) {
            $("#estadoTaller").text("ABIERTO").removeClass("cerrado").addClass("abierto");;
        } else {
            $("#estadoTaller").text("CERRADO").removeClass("abierto").addClass("cerrado");
        }
    }

    // Llamar a la función para obtener la hora de Santiago al cargar la página
    obtenerHoraSantiago();
});