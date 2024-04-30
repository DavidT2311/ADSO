"""
Para un salario hasta de 1500 pesos no hay retencion, para un salario de 1500 pesos a 3000 5%, para un salario mayor de 3000 pesos
8%, imprimir nombre del empleado, salario bruto, valor de retencion, salario neto, pedir nombre y salario
"""

nombre = input("Ingrese su nombre: ")
salario = int(input("Ingrese el salario: "))
retencion = 0
neto = 0


if salario <= 1500:
    print(f"\nEmpleado: {nombre}\nSalario bruto: {salario}\nRetencion 0%: {retencion}\nNeto: {salario}")
elif salario > 1500 and salario <= 3000:
    retencion = salario * 0.05
    neto = salario - retencion
    print(f"\nEmpleado: {nombre}\nSalario bruto: {salario}\nRetencion 5%: {retencion}\nNeto: {neto}")
elif salario > 3000:
    retencion = salario * 0.08 
    neto = salario - retencion
    print(f"\nEmpleado: {nombre}\nSalario bruto: {salario}\nRetencion 8%: {retencion}\nNeto: {neto}")