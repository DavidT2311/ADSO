"""
Pedir 10 numero y decir cual es el numero mayor y cual es el menor
"""

numero1 = 0
mayor = 0
menor = 0

print("Vas a ingresar 10 numeros, y te dire cual es el mayor y el menor")

numero1 = int(input("Ingrese un numero: "))
mayor = numero1
menor = numero1

for i in range(9):
    numero1 = int(input("Ingrese un numero: "))
    if numero1 >= mayor:
        mayor = numero1
    elif numero1 <= menor:
        menor = numero1

print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)