//Expectativas
document.getElementById('expectativas').addEventListener('submit', function(event) {
    var salario = document.getElementById('salario').value;
    var roles = document.getElementById('roles').value

    if (!salario || !roles) {
        alert('Por favor, completa todos los campos obligatorios');
        event.preventDefault();
    }
});

//Desarrollado por Jojhan David Torres Tobon :)
//Desarrollado por Jojhan David Torres Tobon :)