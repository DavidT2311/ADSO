let lista_sexos = [{"Codigo": 1, "Nombre": "Masculino"}, {"Codigo": 2, "Nombre": "Femenino"}]

let lista_ciudades = [{"Codigo": 1, "Nombre": "Medellin"}]

let lista_tipo_documento = [{"Codigo": 1, "Nombre": "TI"}, {"Codigo": 2, "Nombre": "CC"}]

let lista_usuarios = []

let lista_programas = []

class UsuariosModels {
    constructor(tipo_documento, documento, nombre, apellidos, ciudad, sexo, programa) {
        this.Tipo_Documento = tipo_documento;
        this.Documento = documento;
        this.Nombre = nombre;
        this.Apellidos = apellidos;
        this.Ciudad = ciudad;
        this.Sexo = sexo;
        this.Programa = programa;
    }
}

class ProgramasModels {
    constructor(codigo, nombre) {
        this.Codigo = codigo;
        this.Nombre = nombre;
    }
}

const menuPrincipal = () => {
    let opcion;

    do {
        opcion = parseInt(prompt(`Bienvenido, digite una opcion
            1. Usuarios
            2. Tipo de documento
            3. Sexo
            4. Ciudad
            5. Programa
            6. Filtros
            7. Salir`))
        
        switch (opcion) {
            case 1:
                menuUsuarios();
                break;
            case 2:
                menuTiposDocumento();
                break;
            case 3:
                menuSexos();
                break;
            case 4:
                menuCiudades();
                break;
            case 5:
                menuProgramas();
                break;
            case 6:
                menuFiltros();
                break;
            case 7:
                break;
            default:
                alert("Digite una opcion correcta.")
                break;
        }
        
    } while (opcion != 7);

}


const menuUsuarios = () => {
    let opcion;

    do {
        opcion = parseInt(prompt(`Digite una opcion
            1. Listado
            2. Nuevo registro
            3. Salir`))
        
        switch (opcion) {
            case 1:
                alert(listarUsuarios());
                break;
            case 2:
                agregarUsuarios();
                break;
            case 3:
                break;
            default:
                alert("Digite una opcion correcta.")
                break;
        }
        
    } while (opcion != 3);
}

const menuTiposDocumento = () => {
    let opcion;

    do {
        opcion = parseInt(prompt(`Digite una opcion
            1. Listado
            2. Nuevo registro
            3. Salir`))
        
        switch (opcion) {
            case 1:
                alert(listar(lista_tipo_documento));
                break;
            case 2:
                agregar(lista_tipo_documento);
                break;
            case 3:
                break;
            default:
                alert("Digite una opcion correcta.")
                break;
        }
        
    } while (opcion != 3);
}

const menuSexos = () => {
    let opcion;

    do {
        opcion = parseInt(prompt(`Digite una opcion
            1. Listado
            2. Nuevo registro
            3. Salir`))
        
        switch (opcion) {
            case 1:
                alert(listar(lista_sexos));
                break;
            case 2:
                agregar(lista_sexos);
                break;
            case 3:
                break;
            default:
                alert("Digite una opcion correcta.")
                break;
        }
        
    } while (opcion != 3);
}

const menuCiudades = () => {
    let opcion;

    do {
        opcion = parseInt(prompt(`Digite una opcion
            1. Listado
            2. Nuevo registro
            3. Salir`))
        
        switch (opcion) {
            case 1:
                alert(listar(lista_ciudades));
                break;
            case 2:
                agregar(lista_ciudades);
                break;
            case 3:
                break;
            default:
                alert("Digite una opcion correcta.")
                break;
        }
        
    } while (opcion != 3);
}

const menuProgramas = () => {
    let opcion;

    do {
        opcion = parseInt(prompt(`Digite una opcion
            1. Listado
            2. Nuevo registro
            3. Salir`))
        
        switch (opcion) {
            case 1:
                alert(listar(lista_programas));
                break;
            case 2:
                agregar(lista_programas);
                break;
            case 3:
                break;
            default:
                alert("Digite una opcion correcta.")
                break;
        }
        
    } while (opcion != 3);
}

const menuFiltros = () => {
    
}


const listar = (lista) => {
    let mensaje = "";
    if (!lista.length == 0) {
        for (let objeto of lista) {
            mensaje += `Codigo: ${objeto.Codigo}, Nombre: ${objeto.Nombre}\n`;
        } 
    } else {
        mensaje = "La lista esta vacia";
    }
    return mensaje;
}

const agregar = (lista) => {
    let nuevo_registro = {
        "Codigo": parseInt(prompt("Digite el codigo")),
        "Nombre": prompt(prompt("Digite el nombre"))
    }
    lista.push(nuevo_registro);
    alert("Se ha agregado correctamente");
}

const obtenerNombreByCode = (code, lista) => {
    let mensaje = "La lista esta vacia";
    if (!lista.length == 0) {
        for (let objeto of lista) {
            if (objeto.Codigo == code) {
                mensaje = `${objeto.Nombre}`;
            } else {
                mensaje = "No se encontro el codigo";
            }
        }
    }
    return mensaje;
}

const listarUsuarios = () => {
    let mensaje = "La lista esta vacia"
    if (!lista_usuarios.length == 0) {
        for (let objeto of lista_usuarios) {
            mensaje += `Tipo de Documento: ${obtenerNombreByCode(objeto.Tipo_Documento, lista_tipo_documento)}, Documento: ${objeto.Documento}
            Nombre: ${objeto.Nombre}, Apellidos: ${objeto.Apellidos}
            Ciudad: ${obtenerNombreByCode(objeto.Ciudad, lista_ciudades)}, Sexo: ${obtenerNombreByCode(objeto.Sexo, lista_sexos)}
            Programa: ${obtenerNombreByCode(objeto.Programa, lista_programas)}\n`
        }
    }
    return mensaje;
}

const agregarUsuarios = () => {
    let cantidad = parseInt(prompt("Digite la cantidad que desea ingresar"));

    for (let i = 0; i < cantidad; i++) {
        let tipo_documento = parseInt(prompt(`${listar(lista_tipo_documento)}\n
            Digite el codigo del tipo de documento`));
        let documento = parseInt(prompt(`Digite el numero del documento`));
        let nombre = parseInt(prompt(`Digite el nombre`));
        let apellidos = parseInt(prompt(`Digite los apellidos`));
        let ciudad = parseInt(prompt(`${listar(lista_ciudades)}\n
            Digite el codigo de la ciudad`));
        let sexo = parseInt(prompt(`${listar(lista_sexos)}\n
            Digite el codigo del sexo`));
        let programa = parseInt(prompt(`${listar(lista_programas)}\n
            Digite el codigo del programa`));

        nuevo_usuario = UsuariosModels(tipo_documento, documento, nombre, apellidos, ciudad, sexo, programa);
        lista_usuarios.push(nuevo_usuario);
        alert("Se ha ingresado correctamente");
    }
}


menuPrincipal()