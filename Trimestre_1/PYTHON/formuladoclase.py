"""Una ferreteria vende a 3 clientes 3 productos, la información sobre ellos es el nombre del producto, la cantidad
y el precio.
 Debe 1. calcular el valor de la compra por cliente, preguntar si va a pagar a credito(1) o de contado(2)
 2. si paga de contado le hace un descuento del 10% del valor de su compra y si lo hace a credito se le recargara´un 20%
 3. Finalmente, debe de informar cual fue el valor de las compras a credito, el valor de las compras de contado y el valor
total de las ventas de la ferreteria
# se sugiere colocar la misma cantidad y el mismo precio a todos los productos"""
i = 0 # controla clientes
j = 0 # controla productos
pague = 0
acpague = 0
fp = ""
acontado = 0
acredito = 0
for i in range(3): # controla 3 clientes
    j = 0 # para inicializar el ingreso de cada producto
    acpague = 0
    for j in range(3): # controla 3 productos
        nproducto = input("Nombre del producto:")
        cantidad = int(input("Que cantidad se compra:  "))
        precio = int(input("Precio del producto: "))
        pague = cantidad * precio # valor por producto
        acpague = acpague + pague # se acumula
        print("Su compra va en ", acpague)
    fp = int(input("Forma de pago:  (1) credito - (2) contado "))
    if fp == 1:
        acpague = acpague + acpague * 0.2
        print(" el total de su compra es", acpague)
        acredito = acredito + acpague # se acumulan las compras a credito
    else:
        acpague = acpague - acpague * 0.1
        print(" el total de su compra es", acpague)
        acontado = acontado + acpague # se acumulan las compras de contado

print("las ventas a credito fueron ", acredito)
print("las ventas de contado fueron ", acontado)

# calcular el numero mayor y menor de una serie de 10 numeros

