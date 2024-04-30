pago = 0

for i in range (0,5,1):
    horas = float(input("Ingrese las horas: "))
    valor = float(input("Ingrese el valor: "))
    pago += horas * valor

print(f"Cantidad de horas: ", pago)