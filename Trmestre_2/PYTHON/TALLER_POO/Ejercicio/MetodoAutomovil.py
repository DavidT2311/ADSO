#Realizar un programa que permita a un administrador ingresar varios automoviles (marca, modelo, velocidad),
#el programa debe estar en la capacidad de permitir ingresar N cantidad de autos

#Definir cual es el automovil mas rapido de los ingresados, el mas lento de los ingresados

class Automovil:
    def __init__(self):
        self.listaAutomoviles = []
        self.vehiculoVelocidadMayor = {}
        self.vehiculoVelocidadMenor = {}

    def llenar_automoviles(self, nuevoAutomovil):
        self.listaAutomoviles.append(nuevoAutomovil)


    def obtener_velocidad_menor(self):
        velocidades = []
        for objeto in self.listaAutomoviles:
            velocidades.append(objeto.get("Velocidad"))

        velocidadMenor = min(velocidades)
        for objeto in self.listaAutomoviles:
            if velocidadMenor == objeto.get("Velocidad"):
                self.vehiculoVelocidadMenor["Marca"] = objeto.get("Marca")
                self.vehiculoVelocidadMenor["Modelo"] = objeto.get("Modelo")
                self.vehiculoVelocidadMenor["Velocidad"] = objeto.get("Velocidad")


    def obtener_velocidad_mayor(self):
        listaVelocidades = []
        for objeto in self.listaAutomoviles:
            listaVelocidades.append(objeto.get("Velocidad"))

        velocidadMayor = max(listaVelocidades)
        for objeto in self.listaAutomoviles:
            if velocidadMayor == objeto.get("Velocidad"):
                self.vehiculoVelocidadMayor["Marca"] = objeto.get("Marca")
                self.vehiculoVelocidadMayor["Modelo"] = objeto.get("Modelo")
                self.vehiculoVelocidadMayor["Velocidad"] = objeto.get("Velocidad")


    def __str__(self):
        print(self.listaAutomoviles)
        print(self.vehiculoVelocidadMenor)
        print(self.vehiculoVelocidadMayor)