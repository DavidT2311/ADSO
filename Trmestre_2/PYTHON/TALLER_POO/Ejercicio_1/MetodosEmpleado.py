class Empleado:
    def __init__(self):
        self.nombre = ""
        self.sueldo = 0
        self.mensajeImpuestos = ""
        self.__obtener_empleado()

    def __obtener_empleado(self):
        self.nombre = input("Digite el nombre del empleado: ")
        self.sueldo = float(input("Digite el sueldo del empleado: "))
        self.__debe_pagar_impuestos()

    def __debe_pagar_impuestos(self):
        if self.sueldo > 3000:
            self.mensajeImpuestos = "Debe pagar impuestos"
        else:
            self.mensajeImpuestos = "No debe pagar impuestos"
        self.__mostrar_datos()

    def __mostrar_datos(self):
        print(f"Nombre : {self.nombre}\nSueldo : {self.sueldo}\nImpuestos : {self.mensajeImpuestos}")


