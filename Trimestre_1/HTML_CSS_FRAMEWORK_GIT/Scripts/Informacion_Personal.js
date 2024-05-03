//Informacion personal
document.getElementById('informacion_personal').addEventListener('submit', function(event) {
    var nombre = document.getElementById('nombre').value;
    var email = document.getElementById('email').value;
    var telefono = document.getElementById('telefono').value;
    var postal = document.getElementById('postal').value;

    if (!nombre || !email || !telefono) {
        alert('Por favor, completa todos los campos obligatorios');
        event.preventDefault();
    }
});