#Realizar un programa que permita a un administrador ingresar varios automoviles (marca, modelo, velocidad),
#el programa debe estar en la capacidad de permitir ingresar N cantidad de autos

#Definir cual es el automovil mas rapido de los ingresados, el mas lento de los ingresados

from MetodoAutomovil import Automovil

automovil = Automovil()
condicion = 1
while condicion == 1:
    marca = input("Digite la marca del vehiculo: ")
    modelo = input("Digite la modelo del vehiculo: ")
    velocidad = float(input("Digite la velocidad del vehiculo: "))

    nuevoAutomovil = {"Marca": marca, "Modelo": modelo, "Velocidad": velocidad}

    automovil.llenar_automoviles(nuevoAutomovil)

    condicion = int(input("¿Desea ingresar otro automovil?\n1. Si, 2. No: "))

automovil.obtener_velocidad_menor()
automovil.obtener_velocidad_mayor()
automovil.__str__()
