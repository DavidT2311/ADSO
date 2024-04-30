#Ferreteria que va a vender a 3 clientes 3 productos y se puede vender a credito o de contado
#Si es a credito se hace un recargo del 20% del valor de la compra
#Si es de contado se hace un descuento del 10%

cantidad = 0
precio = 0

pago = 0
ACPago = 0
descuento = 0

decision = 0

for i in range(2):
    print("\nIngrese los productos del cliente ", (i+1))
    for j in range(3):
        producto = input(f"Ingrese el producto {(j+1)} :")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = int(input("Ingrese El precio unitario: "))

        pago += cantidad * precio

    decision = int(input("1. Credito \n2. Contado \nSelecione una opcion: "))

    if decision == 1:
        descuento = pago * 0.20
        ACPago = pago - descuento
        print("El precio subtotal es: ", pago)
        print("El cliente ", (i+1), " se le aplicara un descuento del 20%, el pago total es: ", ACPago)
        pago = 0
    elif decision == 2:
        descuento = pago * 0.10
        ACPago = pago + descuento
        print("El precio subtotal es: ", pago)
        print("El cliente ", (i+1), " se le aplicara un recargo del 10%, el pago total es: ", ACPago)
        pago = 0
    else:
        print("Opcion incorrecta")    