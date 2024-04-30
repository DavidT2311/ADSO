desicion = 0
seleccion = 0
dinero = float(input("Ingrese su saldo anterior: "))
ingresos_Antiguos = dinero

while True:
    desicion = int(input("1. Ingresos\n2. Gastos\n3. Otros ingresos\n4. Otros gastos\n5. Fin\nIngresa una opcion: "))
    if desicion == 1:
        print("\nIngresos...\n")
        print("Selecciona 0 para terminar con la ejecucion del ingreso...")
        while True:
            seleccion = float(input("Digite el valor del ingreso: "))
            dinero += seleccion
            if seleccion == 0:
                break
    elif desicion == 2:
        print("\nGastos...\n")
        print("Selecciona 0 para terminar con la ejecucion de los gastos...")
        while True:
            seleccion = float(input("Digite el valor del gasto: "))
            dinero -= seleccion
            if seleccion == 0:
                break
    elif desicion == 3:
        print("\nOtros ingresos...\n")
        print("Selecciona 0 para terminar con la ejecucion del ingreso...")
        while True:
            seleccion = float(input("Digite el valor del ingreso: "))
            dinero += seleccion
            if seleccion == 0:
                break
    elif desicion == 4:
        print("\nOtros gastos...\n")
        print("Selecciona 0 para terminar con la ejecucion de los gastos...")
        while True:
            seleccion = float(input("Digite el valor del gasto: "))
            dinero -= seleccion
            if seleccion == 0:
                break
    elif desicion == 5:
        dinero = dinero - 2000
        print("\nFin...\n")
        print(f"Los ingresos a comienzo de  mes fueron de ${dinero}")
        print(f"Se le aplico un interes de $2000 y se le cobro una cuota de manejo de $4000\nEl total al final del mes fue ${dinero}")
        break
    else:
        print("\nOpcion incorrecta, ingresa otro valor...\n")
    