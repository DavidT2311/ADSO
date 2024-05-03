//Consentimiento
document.getElementById('consentimiento').addEventListener('submit', function(event) {
    var check = document.getElementById('check').checked;

    if (!check) {
        alert('Por favor, acepta los terminos y condiciones para continuar');
        event.preventDefault();
    } else {
        alert('!Gracias por tu interes en colaborar con nosotros en este proyecto de desarrollo de software¡')
    }
});

//Desarrollado por Jojhan David Torres Tobon :)
//Desarrollado por Jojhan David Torres Tobon :)