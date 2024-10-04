from Estudiante import Estudiante
from MetodosEstudiantes import MetodosEstudiantes

listaEstudiantes = []

while True:
    print("Para terminar escribe salir")
    nombre = input("Digite el nombre del estudiante: ")
    if nombre.lower() == "salir":
        break

    cantidadNotas = int(input("Digite la cantidad de notas: "))
    listaNotas = []
    for i in range(cantidadNotas):
        nota = float(input(f"Digite la nota {i+1}: "))
        listaNotas.append(nota)

    listaEstudiantes.append(Estudiante.obtener_Datos(nombre, listaNotas))

MetodosEstudiantes(listaEstudiantes)
