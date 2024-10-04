class Persona:
    def cargar_datos(self, identificacion, nombre, edad):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")
