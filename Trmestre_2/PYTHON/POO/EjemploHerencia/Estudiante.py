from Persona import Persona

class Estudiante(Persona):

    def cargar_datos(self, identificacion, nombre, edad, notas):
        Persona.cargar_datos(self, identificacion, nombre, edad)
        self.notas = notas

    def comer(self):
        Persona.comer(self)
        print(f"Un estudiante llamado {self.nombre} esta comiendo")
