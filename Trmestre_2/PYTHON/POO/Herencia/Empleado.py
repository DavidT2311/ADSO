from Asesor import Asesor

class Empleado(Asesor):

    def __init__(self):
        Asesor.__init__(self)
        self.celular = ""
        self.nombre = ""

    def obtener_datos(self, correo, direccion, apellido, telefono, celular, nombre):
        Asesor.obtener_datos(self, correo, direccion, apellido, telefono)
        self.celular = celular
        self.nombre = nombre


    def __str__(self):
        Asesor.__str__(self)
        print(f"Celular : {self.celular}, Nombre : {self.nombre}")


