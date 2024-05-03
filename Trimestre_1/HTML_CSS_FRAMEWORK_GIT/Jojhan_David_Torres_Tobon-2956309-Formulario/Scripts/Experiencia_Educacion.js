//Experiencia y educacion
document.getElementById('experiencia_educacion').addEventListener('submit', function(event) {
    var experiencia_laboral = document.getElementById('experiencia_laboral').value;
    var educacion = document.getElementById('educacion').value;
    var certificaciones = document.getElementById('certificaciones').value;

    if (!experiencia_laboral || !educacion || !certificaciones) {
        alert('Por favor, completa todos los campos obligatorios');
        event.preventDefault();
    }
});

//Desarrollado por Jojhan David Torres Tobon :)
//Desarrollado por Jojhan David Torres Tobon :)