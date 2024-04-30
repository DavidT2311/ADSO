numero7 = 0
numeroAuxiliar = 17

for i in range(numeroAuxiliar, 31, 1):
    print(f"Tabla del {numeroAuxiliar}\n")
    j = 1
    for j in range(11):
        print(f"{numeroAuxiliar} * {j} = {(numeroAuxiliar * j)}")
        if j == 7:
            numero7 += numeroAuxiliar * j
    numeroAuxiliar +=1
    print("\n")

print(f"La suma de los multiplos de 7 es {numero7}")