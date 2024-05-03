//Disponibilidad
document.getElementById('disponibilidad').addEventListener('submit', function(event) {
    var disponibilidad_semanal = document.getElementById('disponibilidad_semanal').value;
    var fecha_inicio = document.getElementById('fecha_inicio').value;
    var fecha_fin = document.getElementById('fecha_fin').value;

    if (!disponibilidad_semanal || !fecha_inicio || !fecha_fin) {
        alert('Por favor, completa todos los campos obligatorios');
        event.preventDefault();
    }
});

//Desarrollado por Jojhan David Torres Tobon :)
//Desarrollado por Jojhan David Torres Tobon :)