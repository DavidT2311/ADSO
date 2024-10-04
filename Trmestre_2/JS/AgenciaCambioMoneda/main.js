const menuInicial = () => {
    let COP;
    let cambio;
    alert("Agencia de cambio");

    do {
        cambio = parseInt(prompt(`Digite a que moneda desea convertir
            1. Elegir cantidad
            2. EUR
            3. USD
            4. Salir
            `))

            switch (cambio) {
                case 1:
                    COP = parseFloat(prompt("Digite la cantidad en COP que desea convertir"));
                    break;
                case 2:
                    moneda_convertida = USD(COP);
                    break;
                case 3:
                    moneda_convertida = EUR(COP);
                    break;
                case 4:
                    break;
                default:
                    alert("Algo salio mal, intentalo de nuevo");
                    break;
            }

    } while (cambio != 4);

}

const EUR = (COP) => {
    alert(`La conversion de ${COP} COP a EUR es:  ${COP / 4000}`);
}

const USD = (COP) => {
    alert(`La conversion de ${COP} COP a USD es:  ${COP / 4433}`);
}

menuInicial()
