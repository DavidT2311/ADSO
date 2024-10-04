class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = modelo

    def __str__(self):
        return f"La marca es: {self.marca}\nEl modelo es {self.modelo}\nEl color es: {self.color}"


taxi = Auto("Audi", "A8", "Rojo")
print(taxi.__str__())
