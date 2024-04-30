#Mercado de tres productos, se pedira la cantidad, el precio, calcular el subtotal, el descuento y el neto
#imprimir al final el acumulado del subtotal, el acumulado del descuento y el acumulado del neto

Producto =""
cantidad = 0
precio = 0
subtotal = 0
descuento = 0
neto = 0
decision = 0


for i in range (3):
    producto = input("ingrese producto: ")
    cantidad = float (input("ingrese cantidad: "))
    precio = float (input ("ingrese precio de producto: "))
    subtotal += cantidad * precio 

"""
descuento = subtotal * 0.10
neto = subtotal - descuento

print ("subtotal: ", subtotal)
print ("descuento:", descuento)
print ("neto:", neto)
"""

decision = int(input("1. Credito \n2. Contado \nSelecione una opcion: "))

if decision == 1:
    descuento = subtotal * 0.20
    neto = subtotal - descuento
    print("El precio subtotal es: ", subtotal)
    print("El cliente ", (i+1), " se le aplicara un descuento del 20%, el pago total es: ", neto)
    subtotal = 0
elif decision == 2:
    descuento = subtotal * 0.10
    neto = subtotal + descuento
    print("El precio subtotal es: ", subtotal)
    print("El cliente ", (i+1), " se le aplicara un recargo del 10%, el pago total es: ", neto)
    subtotal = 0
else:
    print("Opcion incorrecta")