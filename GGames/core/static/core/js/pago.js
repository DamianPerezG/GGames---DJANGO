document.addEventListener('DOMContentLoaded', function () {
    
    const formPago = document.querySelector('form');

    
    formPago.addEventListener('submit', function(event) {
        event.preventDefault(); 


        const nombre = document.getElementById('nombre').value.trim();
        const numeroTarjeta = document.getElementById('numero').value.trim();
        const vencimiento = document.getElementById('fecha').value.trim();
        const codigoSeguridad = document.getElementById('codigo').value.trim();

        if (nombre === '' || numeroTarjeta === '' || vencimiento === '' || codigoSeguridad === '') {
            alert('Por favor, completa todos los campos.');
            return;
        }

        if (!/^\d{16}$/.test(numeroTarjeta.replace(/-/g, ''))) {
            alert('Por favor, ingresa un número de tarjeta válido.');
            return;
        }

        if (!/^\d{2}\/\d{2}$/.test(vencimiento)) {
            alert('Por favor, ingresa una fecha de vencimiento válida (MM/AA).');
            return;
        }

        if (!/^\d{3}$/.test(codigoSeguridad)) {
            alert('Por favor, ingresa un código de seguridad válido.');
            return;
        }

        
        setTimeout(() => {
            
            alert('¡Pago realizado con éxito!');

            window.location.href = 'index.html';
        }, 5000);
    });
});
