from Persona import Persona

class Asesor(Persona):

    def __init__(self):
        Persona.__init__(self)
        self.apellido = ""
        self.telefonoFijo = ""

    def obtener_datos(self, correo, direccion, apellido, telefono):
        Persona.obtener_datos(self, correo, direccion)
        self.apellido = apellido
        self.telefonoFijo = telefono

    def __str__(self):
        print(f"Correo: {self.correo}, Direccion : {self.direccion}, Apellido: {self.apellido}, Telefono : {self.telefonoFijo}")

