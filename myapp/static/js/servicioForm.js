document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('mantenimiento_form');
    const zonaSelect = document.getElementById('zona');
    const piezasSelect = document.getElementById('piezas');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        validateForm();
    });

    zonaSelect.addEventListener('change', () => {
        updatePiezasOptions();
        piezasSelect.disabled = zonaSelect.value === '';
    });

    function validateForm() {
        const mecanico = document.getElementById('mecanico');
        const zona = document.getElementById('zona');
        const piezas = document.getElementById('piezas');
        const comentarios = document.getElementById('comentarios');

        let isValid = true;

        // Validate Mecánico
        if (mecanico.value === '') {
            showError(mecanico, 'error_mecanico', 'Seleccione un mecánico');
            isValid = false;
        } else {
            hideError(mecanico, 'error_mecanico');
        }

        // Validate Zona de Mantenimiento
        if (zona.value === '') {
            showError(zona, 'error_zona', 'Seleccione la zona de mantenimiento');
            isValid = false;
        } else {
            hideError(zona, 'error_zona');
        }

        // Validate Piezas Reemplazadas
        if (piezas.value === '') {
            showError(piezas, 'error_piezas', 'Seleccione una pieza reemplazada');
            isValid = false;
        } else {
            hideError(piezas, 'error_piezas');
        }

        // Comentarios Adicionales es opcional, no se valida si está vacío

        if (isValid) {
            form.submit();
        }
    }

    function showError(element, errorElementId, message) {
        const errorElement = document.getElementById(errorElementId);
        errorElement.textContent = message;
        errorElement.style.display = 'block';
        element.classList.add('is-invalid');
    }

    function hideError(element, errorElementId) {
        const errorElement = document.getElementById(errorElementId);
        errorElement.style.display = 'none';
        element.classList.remove('is-invalid');
    }

    function updatePiezasOptions() {
        const zona = zonaSelect.value;
        const piezasOptions = piezasSelect.querySelectorAll('option');

        const compatibility = {
            'Techo': ['Antena', 'Techo corredizo', 'Revestimiento interior del techo'],
            'Motor': ['Motor', 'Bateria', 'Bujia'],
            'Cajuela': ['Llanta de repuesto', 'Kit de herramientas', 'Alfombra de la cajuela'],
            'Capó': ['Amortiguadores de capó', 'Cerradura de capó', 'Aislante del capó'],
            'Puertas': ['Manija de puerta', 'Ventana de puerta', 'Cerradura de puerta'],
            'Chasis': ['Suspensión', 'Ruedas', 'Frenos']
        };

        piezasOptions.forEach(option => {
            if (option.value === "") return; // Skip the default "Seleccione una pieza" option
            if (compatibility[zona] && compatibility[zona].includes(option.value)) {
                option.disabled = false;
            } else {
                option.disabled = true;
            }
        });
    }
});
