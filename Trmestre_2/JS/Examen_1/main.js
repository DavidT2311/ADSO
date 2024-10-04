const menuInicial = () => {
    let nombre = "";
    let opcion = 0;

    nombre = prompt("Digite su nombre");

    do {
        opcion = parseInt(prompt(`Hola ${nombre}, digite una opcion
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Salir
            `));

        switch (opcion) {
            case 1:
                suma(nombre);
                break;
            case 2:
                resta(nombre);
                break;
            case 3:
                multiplicacion(nombre);
                break;
            case 4:
                break;    
            default:
                alert("Ha ocurrido un error, intentalo de nuevo");
                break;
        }
    } while (opcion != 4);
    

}

const suma = (nombre) => {
    let mensaje_tablas = `${nombre} estas son las tablas\n`;
    let numero_elegido = 0;

    numero_elegido = parseFloat(prompt(`${nombre}, digite el numero que desea ingresar`));
    for (let i = 0; i < 10; i++) {
        mensaje_tablas += `${numero_elegido} + ${i+1} = ${numero_elegido + (i+1)}\n`
    };    
    alert(mensaje_tablas);
}

const resta = (nombre) => {
    let mensaje_tablas = `${nombre} estas son las tablas\n`;

    let numero_elegido = parseInt(prompt(`${nombre}, digite el numero que desea ingresar`));
    for (let i = 0; i < 10; i++) {
        mensaje_tablas += `${numero_elegido} - ${i+1} = ${numero_elegido - (i+1)}\n`
    };
    
    alert(mensaje_tablas);
}

const multiplicacion = (nombre) => {
    let mensaje_tablas = `${nombre} estas son las tablas\n`;

    let numero_elegido = parseInt(prompt(`${nombre}, digite el numero que desea ingresar`));
    for (let i = 0; i < 10; i++) {
        mensaje_tablas += `${numero_elegido} * ${i+1} = ${numero_elegido * (i+1)}\n`
    };
    
    alert(mensaje_tablas);
}


menuInicial()
