class Notas():
    def __init__(self):
        self.notas = []

    def llenarDatos(self, nota):
        self.notas.append(nota)

    def _calcular_promedio(self):
        promedio = sum(self.notas) / len(self.notas)
        return promedio

    def _definir_estado(self, promedio):
        promedio = self._calcular_promedio()
        estado = ""
        if promedio >= 1 and promedio < 6:
            estado = "Pierde"
        elif promedio >= 6 and promedio <= 10:
            estado = "Gana"
        else:
            return "Hubo un error con los datos"
        return estado

    def mostrar_datos(self):
        promedio = self._calcular_promedio()
        estado = self._definir_estado(promedio)
        return f"Estado: {promedio}\nPromedio: {estado}"


