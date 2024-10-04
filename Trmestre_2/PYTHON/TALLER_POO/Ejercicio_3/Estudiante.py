class Estudiante:
    def __init__(self):
        self.nombre = ""
        self.listaNotas = []
        self.promedioNotas = 0
        self.estado = ""
        self.__obtener_datos()

    def __obtener_datos(self):
        self.nombre = input("Digite el nombre del estudiante: ")
        for i in range(6):
            nota = float(input(f"Digite la nota #{i+1}: "))
            self.listaNotas.append(nota)
        self.__obtener_promedio()

    def __obtener_promedio(self):
        for nota in self.listaNotas:
            self.promedioNotas += nota
        self.promedioNotas = self.promedioNotas / len(self.listaNotas)
        self.__definir_estado()

    def __definir_estado(self):
        if self.promedioNotas >= 0 and self.promedioNotas <= 5:
            self.estado = "Pierde"
        elif self.promedioNotas > 5 and self.promedioNotas <= 10:
            self.estado = "Gana"
        else:
            self.estado = "Notas incorrectas"
        self.__mostrar_datos()
    def __mostrar_datos(self):
        print(f"Lista notas : {self.listaNotas}")
        print(f"Nombre : {self.nombre}\nPromedio : {self.promedioNotas}\nEstado : {self.estado}")
