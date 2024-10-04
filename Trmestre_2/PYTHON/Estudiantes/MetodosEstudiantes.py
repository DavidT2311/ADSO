class MetodosEstudiantes:
    def __init__(self, listaEstudiantes):
        self.listaEstudiantes = listaEstudiantes
        self.listaDatos = {}
        self.__promedio_Notas_Estudiante()

    def __promedio_Notas_Estudiante(self):
        i = 0
        for objeto in self.listaEstudiantes:
            notas = objeto["Notas"]
            promedio = sum(notas) / len(notas)
            self.listaEstudiantes[i].setdefault("Promedio", promedio)
            i += 1
        self.__promedio_General()

    def __promedio_General(self):
        promedioEstudiante = 0
        cantidadEstudiantes = 0
        for objeto in self.listaEstudiantes:
            promedioEstudiante += objeto["Promedio"]
            cantidadEstudiantes += 1
        self.listaDatos.setdefault("PromedioGeneral", (promedioEstudiante / cantidadEstudiantes))
        self.__estudiantes_Ganados()


    def __estudiantes_Ganados(self):
        estudiantesGanados = 0
        for objeto in self.listaEstudiantes:
            if objeto["Promedio"] >= 6:
                estudiantesGanados += 1
        self.listaDatos.setdefault("EstudiantesGanados", estudiantesGanados)
        self.__estudiantes_Perdidos()

    def __estudiantes_Perdidos(self):
        estudiantesPerdidos = 0
        for objeto in self.listaEstudiantes:
            if objeto["Promedio"] < 6:
                estudiantesPerdidos += 1
        self.listaDatos.setdefault("EstudiantesPerdidos", estudiantesPerdidos)
        self.__mostrar_Datos()

    def __mostrar_Datos(self):
        for datos in self.listaEstudiantes:
            print(datos)
        print(self.listaDatos)




