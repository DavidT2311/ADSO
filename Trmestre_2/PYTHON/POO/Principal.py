from NotasPOO import Notas

notas = Notas()
for i in range(6):
    nota = float(input(f"Digite las nota {i+1}: "))
    notas.llenarDatos(nota)

print(notas.mostrar_datos())
