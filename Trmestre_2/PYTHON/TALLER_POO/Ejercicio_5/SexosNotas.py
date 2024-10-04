class SexosNotas:
    def __init__(self):
        self.listaPersonas = []
        self.datosGenerales = {}
        #self.__obtener_datos()
        self.__actualizar_notas_mujer()

    def __obtener_datos(self):
        print("Digitara 10 sexos y 10 notas")
        for i in range(10):
            persona = {}
            sexo = input(f"Digite el sexo {i+1} (Hombre - Mujer): ")
            nota = float(input(f"Digite la nota {i+1}: "))
            persona.update({"Sexo" : sexo})
            persona.update({"Nota" : nota})
            self.listaPersonas.append(persona)
        self.__actualizar_notas_mujer()


    def __actualizar_notas_mujer(self):
        iterador = 0
        for objeto in self.listaPersonas:
            sexo = objeto["Sexo"]
            nota = objeto["Nota"]
            if sexo.lower() == "mujer":
                nota -= 3
                self.listaPersonas[iterador].update({"Nota" : nota})
            iterador += 1
        self.__actualizar_notas_hombre()

    def __actualizar_notas_hombre(self):
        iterador = 0
        for objeto in self.listaPersonas:
            sexo = objeto["Sexo"]
            nota = objeto["Nota"]
            if sexo.lower() == "hombre":
                nota += 3
                self.listaPersonas[iterador].update({"Nota": nota})
            iterador += 1
        self.__definir_cantidad_notas_perdidas()

    def __definir_cantidad_notas_perdidas(self):
        cantidadNotasPerdidas = 0
        for objeto in self.listaPersonas:
            nota = objeto["Nota"]
            if nota <= 5:
                cantidadNotasPerdidas += 1
        self.datosGenerales.update({"CantidadNotasPerdidas" : cantidadNotasPerdidas})
        self.__definir_cantidad_notas_ganadas()

    def __definir_cantidad_notas_ganadas(self):
        cantidadNotasGanadas = 0
        for objeto in self.listaPersonas:
            nota = objeto["Nota"]
            if nota > 5:
                cantidadNotasGanadas += 1
        self.datosGenerales.update({"CantidadNotasGanadas" : cantidadNotasGanadas})
        self.__definir_promedio_notas_perdidas()

    def __definir_promedio_notas_perdidas(self):
        promedioNotasPerdidas = 0
        for objeto in self.listaPersonas:
            nota = objeto["Nota"]
            if nota <= 5:
                promedioNotasPerdidas += nota
        promedioNotasPerdidas = round(promedioNotasPerdidas / self.datosGenerales["CantidadNotasPerdidas"], 2)
        self.datosGenerales.update({"PromedioNotasPerdidas" : promedioNotasPerdidas})
        self.__definir_promedio_notas_ganadas()

    def __definir_promedio_notas_ganadas(self):
        promedioNotasGanadas = 0
        for objeto in self.listaPersonas:
            nota = objeto["Nota"]
            if nota > 5:
                promedioNotasGanadas += nota
        promedioNotasGanadas = round(promedioNotasGanadas / self.datosGenerales["CantidadNotasGanadas"], 2)
        self.datosGenerales.update({"PromedioNotasGanadas" : promedioNotasGanadas})
        self.__definir_nota_mayor()

    def __definir_nota_mayor(self):
        listaNotasTotales = []
        for objeto in self.listaPersonas:
            listaNotasTotales.append(objeto["Nota"])
        notaMayor = max(listaNotasTotales)
        self.datosGenerales.update({"NotaMayor" : notaMayor})
        self.__definir_nota_menor()


    def __definir_nota_menor(self):
        listaNotasTotales = []
        for objeto in self.listaPersonas:
            listaNotasTotales.append(objeto["Nota"])
        notaMenor = min(listaNotasTotales)
        self.datosGenerales.update({"NotaMenor": notaMenor})
        self.__mostrar_datos()

    def __mostrar_datos(self):
        print("Datos recogidos y modificados : ")
        for objeto in self.listaPersonas:
            print(objeto)
        print("\nDatos generales : ")
        print(self.datosGenerales)


