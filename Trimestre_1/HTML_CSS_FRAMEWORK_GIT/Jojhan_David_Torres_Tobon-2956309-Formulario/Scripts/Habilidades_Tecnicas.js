//Habilidades tecnicas
document.getElementById('habilidades_tecnicas').addEventListener('submit', function(event) {
    var lenguajes = document.getElementById('lenguajes').value;
    var herramientas = document.getElementById('herramientas').value;
    var experiencia = document.getElementById('experiencia').value;

    if (!lenguajes || !herramientas || !experiencia) {
        alert('Por favor, completa todos los campos obligatorios');
        event.preventDefault();
    }
});

//Desarrollado por Jojhan David Torres Tobon :)
//Desarrollado por Jojhan David Torres Tobon :)