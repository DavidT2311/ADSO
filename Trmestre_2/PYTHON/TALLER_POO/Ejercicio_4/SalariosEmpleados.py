class SalariosEmpleados:
    def __init__(self):
        self.listaEmpleados = []
        self.datosGenerales = {}
        self.__obtener_datos()

    def __obtener_datos(self):
        print("Ingresaras 10 empleados")
        for i in range(3):
            empleado = {}
            nombre = input(f"Digite el nombre del empleado {i+1}: ")
            listaNotas = []
            print("Ingresaras 10 notas")
            for j in range(3):
                while True:
                    nota = float(input(f"Digite la nota {j + 1} (1 - 1000): "))
                    if nota < 1 or nota > 1000:
                        print("Digite la nota correctamente")
                    else:
                        listaNotas.append(nota)
                        break
            empleado.update({"Nombre": nombre})
            empleado.update({"Notas": listaNotas})
            self.listaEmpleados.append(empleado)
        self.__sacar_total_salario()


    def __sacar_total_salario(self):
        iterador = 0
        for objeto in self.listaEmpleados:
            salarioTotal = sum(objeto["Notas"])
            self.listaEmpleados[iterador].update({"SalarioTotal": salarioTotal})
            iterador += 1
        self.__verificar_aumento_sueldo()

    def __verificar_aumento_sueldo(self):
        iterador = 0
        for objeto in self.listaEmpleados:
            nombre = objeto["Nombre"]
            salarioTotal = objeto["SalarioTotal"]

            if nombre.lower() == "susana":
                aumento = salarioTotal * 0.20
                salarioTotal = salarioTotal + aumento
                self.listaEmpleados[iterador].update({"SalarioTotal" : salarioTotal})
            elif nombre.lower() == "jessica":
                aumento = salarioTotal * 0.15
                salarioTotal = salarioTotal + aumento
                self.listaEmpleados[iterador].update({"SalarioTotal" : salarioTotal})
            elif nombre.lower() == "wilson":
                aumento = salarioTotal * 0.10
                salarioTotal = salarioTotal + aumento
                self.listaEmpleados[iterador].update({"SalarioTotal" : salarioTotal})
            iterador += 1
        self.__calcular_precios_generales()

    def __calcular_precios_generales(self):
        salarioTotal = 0
        for objeto in self.listaEmpleados:
            salarioTotal += objeto["SalarioTotal"]
        self.datosGenerales.update({"SalarioTotal" : salarioTotal})
        self.__calcular_promedio()

    def __calcular_promedio(self):
        promedio = self.datosGenerales["SalarioTotal"] / len(self.listaEmpleados)
        self.datosGenerales.update({"Promedio" : promedio})
        self.__definir_salario_mayor()

    def __definir_salario_mayor(self):
        listaSalariosTotales = []
        for objeto in self.listaEmpleados:
            listaSalariosTotales.append(objeto["SalarioTotal"])
        salarioMayor = max(listaSalariosTotales)
        self.datosGenerales.update({"SalarioMayor" : salarioMayor})
        self.__definir_salario_menor()

    def __definir_salario_menor(self):
        listaSalariosTotales = []
        for objeto in self.listaEmpleados:
            listaSalariosTotales.append(objeto["SalarioTotal"])
        salarioMenor = min(listaSalariosTotales)
        self.datosGenerales.update({"SalarioMenor" : salarioMenor})
        self.__mostrar_datos()

    def __mostrar_datos(self):
        print("Empleados : ")
        for objeto in self.listaEmpleados:
            print(objeto)
        print("\nDatos generales : ")
        print(self.datosGenerales)







