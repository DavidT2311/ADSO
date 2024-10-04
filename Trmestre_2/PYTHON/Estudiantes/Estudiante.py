class Estudiante:
    def obtener_Datos(nombre, listaNotas):
        datosEstudiante = {}
        datosEstudiante.setdefault("Estudiante", nombre)
        datosEstudiante.setdefault("Notas", listaNotas)
        return datosEstudiante
