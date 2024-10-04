let lista_usuarios = [];

function UsuarioModel(usuario, pass) {
    this.usuario = usuario;
    this.pass = pass;
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
                mensaje = "Bienvenido";
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

menuInicial();