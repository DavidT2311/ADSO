class Sueldos:
    def __init__(self):
        self.listaSueldos = []
        self.promedioSueldos = 0
        self.sueldoMayor = 0
        self.sueldoMenor = 0
        self.estado = ""
        self.__obtener_sueldos()

    def __obtener_sueldos(self):
        for i in range(5):
            sueldo = float(input(f"Digite el sueldo {i+1}: "))
            self.listaSueldos.append(sueldo)
        self.__obtener_promedio_sueldos()

    def __obtener_promedio_sueldos(self):
        for sueldo in self.listaSueldos:
            self.promedioSueldos += sueldo
        self.promedioSueldos = self.promedioSueldos / len(self.listaSueldos)
        self.__obtener_sueldo_mayor()

    def __obtener_sueldo_mayor(self):
        self.sueldoMayor = max(self.listaSueldos)
        self.__obtener_sueldo_menor()

    def __obtener_sueldo_menor(self):
        self.sueldoMenor = min(self.listaSueldos)
        self.__calcular_estado()

    def __calcular_estado(self):
        if self.promedioSueldos >= 1 and self.promedioSueldos <= 4000000:
            self.estado = "Sueldo basico"
        elif self.promedioSueldos > 4000000 and self.promedioSueldos <= 10000000:
            self.estado = "Sueldo medio"
        elif self.promedioSueldos > 10000000 and self.promedioSueldos <= 20000000:
            self.estado = "Sueldo alto"
        self.__mostrar_datos()


    def __mostrar_datos(self):
        print(f"Lista de sueldos : {self.listaSueldos}")
        print(f"Promedio de los sueldos : {self.promedioSueldos}\nSueldo mayor : {self.sueldoMayor}")
        print(f"Sueldo menor : {self.sueldoMenor}\nEstado : {self.estado}")
