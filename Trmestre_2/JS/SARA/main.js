let lista_usuarios = [];
let lista_empleados = [];
let lista_empresas = [];

class UsuarioModel { //Modelo para los usuarios
    constructor(usuario, pass) {
        this.usuario = usuario;
        this.pass = pass;
    }
};

class EmpleadoModel {
    constructor (documento, nombre, apellido, ID_empresa) { //Modelo para los empleados
        this.documento = documento;
        this.nombre = nombre;
        this.apellido = apellido;
        this.ID_empresa = ID_empresa;
    }
};

class EmpresaModel {
    constructor (NIT, nombre) { //Modelo para los empleados
        this.NIT = NIT;
        this.nombre = nombre;
    }
};

const menuInicial = () => {
    let opcion;

    do {
        opcion = parseInt(prompt(`Bienvenido, digite una opcion
            1. Login
            2. Registro
            3. Salir
            `)) 

        switch (opcion) {
            case 1:
                userLogin();
                break;
            case 2:
                userRegister();
                break;
            case 3:
                break;
            default:
                alert("Ha ocurrido un error");
                break;
        }
    } while (opcion != 3);



};

const userLogin = () => {
    let usuario;
    let pass;

    if (!(lista_usuarios.length == 0)) {
        usuario = prompt(`Digite el usuario`);
        pass = prompt(`Digite la contraseña`);

        let mensaje = "";
        for (let user of lista_usuarios) {
            if (user.usuario == usuario && user.pass == pass) {
                menuEmpleadosEmpresas();
                break;
            }
            else {
                mensaje = "Credenciales incorrectas";
            };
        };
        alert(mensaje);
    } else {
        let opcion_agregar_usuario;

        do {
            opcion_agregar_usuario = parseInt(prompt(`No se encontraron usuarios, ¿Desea registrarse?
                1. Si
                2. No
                `));
            
            switch (opcion_agregar_usuario) {
                case 1:
                    userRegister();
                    break;
                case 2:
                    break;
                default:
                    alert("Digite una opcion correcta");
                    break;
            };
        } while(opcion_agregar_usuario != 1 && opcion_agregar_usuario != 2);
        
    };
};


const userRegister = () => {
    let usuario;
    let pass;

    usuario = prompt(`Digite el usuario`);
    pass = prompt(`Digite la contraseña`);

    nuevo_usuario = new UsuarioModel(usuario, pass);
    lista_usuarios.push(nuevo_usuario);

    alert("Se ha ingresado correctamente");
};

const menuEmpleadosEmpresas = () => {
    let opcion;

    do {
        opcion = parseInt(prompt(`Bienvenido, digite una opcion
            1. Empleados
            2. Empresas
            3. Salir
            `)) 

        switch (opcion) {
            case 1:
                menuEmpleados();
                break;
            case 2:
                menuEmpresas();
                break;
            case 3:
                break;
            default:
                alert("Ha ocurrido un error");
                break;
        }
    } while (opcion != 3);

}

const menuEmpleados = () => {
    let opcion;
    do {
        opcion = parseInt(prompt(
            `Eliga una opcion
            1. Listar empleados
            2. Ingresar un empleado
            3. Actualizar un empleado
            4. Eliminar un empleado
            5. Volver al menu de empleados - empresas
            `
        ));

        //Switch para elegir un metodo de los empleados
        switch (opcion) {
            case 1:
                break;
            case 2:
                ingresarEmpleado();
                break;
            case 3:
                
                break;
            case 4:
                
                break;
            case 5:
                break;
            default:
                alert("Digite una opcion correcta");
        }
    } while (opcion != 5);
}

const menuEmpresas = () => {
    let opcion;
    do {
        opcion = parseInt(prompt(
            `Eliga una opcion
            1. Listar empresas
            2. Ingresar una empresa
            3. Actualizar una empresa
            4. Eliminar una empresa
            5. Volver al menu de empleados - empresas
            `
        ));

        //Switch para elegir un metodo de las empresas
        switch (opcion) {
            case 1:
                break;
            case 2:
                ingresarEmpresa();
                break;
            case 3:
                
                break;
            case 4:
                
                break;
            case 5:
                break;
            default:
                alert("Digite una opcion correcta");
        }
    } while (opcion != 5);
}

const ingresarEmpleado = () => {
    //Obtiene la cantidad de empleados que registrara
    let cantidad = parseInt(prompt("Digite la cantidad de empleados que desea guardar"));

    if (!lista_empresas.length == 0) {
        for (let i = 0; i < cantidad; i++) {
            let documento = parseInt(prompt("Digite el documento del empleado"));
            let nombre = prompt("Digite el nombre del empleado");
            let apellido = prompt("Digite el apellido del empleado");

            do {
                let NIT = parseInt(prompt(`${generarListaEmpresas()}\n Digite el NIT de la empresa`));

                estado = vericarNITEmpresa(NIT);
                if (estado == false) {
                    alert("El NIT de la empresa no existe");
                }
            } while (estado == false);

            let nuevo_empleado = new EmpleadoModel(documento, nombre, apellido, NIT);
            if (!lista_empleados.length == 0) {
                for (let objeto of lista_empleados) {
                    if (documento == objeto.documento) {
                        alert("El empleado ya existe");
                        break;
                    } else {
                        lista_empleados.push(nuevo_empleado);
                        alert("Se ha ingresado el programa correctamente");
                        break;
                    };
                };
            } else {
                lista_empleados.push(nuevo_empleado);
                alert("Se ha ingresado el programa correctamente");
            };
        };
    } else {
        alert("No hay empresas para vincular el empleado");
    }
};


const ingresarEmpresa = () => {
    //Obtiene la cantidad de empresas que registrara
    let cantidad = parseInt(prompt("Digite la cantidad de empresas que desea guardar"));

    for (let i = 0; i < cantidad; i++) {
        let NIT = parseInt(prompt("Digite la id de la empresa"));
        let nombre = prompt("Digite el nombre de la empresa");

        let nueva_empresa = new EmpresaModel(NIT, nombre);

        if (!lista_empresas.length == 0) {
            for (let objeto of lista_empresas) {
                if (NIT == objeto.NIT) {
                    alert("La empresa ya existe");
                    break;
                } else {
                    lista_empresas.push(nuevo_empleado);
                    alert("Se ha ingresado la empresa correctamente");
                    break;
                };
            };
        } else {
            lista_empresas.push(nueva_empresa);
            alert("Se ha ingresado la empresa correctamente");
        };
    };
};

const generarListaEmpresas = () => {
    let mensaje_lista_empresas = "";

    for (let objeto of lista_empresas) {
        mensaje_lista_empresas += `ID : ${objeto.NIT}, Nombre : ${objeto.nombre}`;
    }
    return mensaje_lista_empresas;
}

const vericarNITEmpresa = NIT => {
    estado = false;
    for (let objeto of lista_empresas) {
        if (objeto.NIT == NIT) {
            estado = true;
        }
    }
    return estado;
}




menuInicial();