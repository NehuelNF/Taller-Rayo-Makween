document.addEventListener("DOMContentLoaded", function() {

    const popoverButton = document.querySelector(".btnn");

    var popover = new bootstrap.Popover(popoverButton, {
        title: 'Carrito de compra',
        content: "! El carrito no esta disponible de momento ¡",
        trigger: "hover",
        container: 'body'
    });

    popoverButton.addEventListener('click', function () {
        popover.toggle();
    });
})