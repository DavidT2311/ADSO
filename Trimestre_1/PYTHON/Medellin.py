edad = 0
sexo = 0
estado_civil = 0

HCasados = 0
MCasadas = 0
HSolteros = 0
MSolteras = 0
Menores = 0

for i in range(6):
    edad = int(input("Ingese su edad: "))
    if edad < 18:
        print("Lo sentimos no cumples con la mayoria de edad")
        Menores += 1
    elif edad <= 0 and edad >= 150:
        print("La edad que has ingresado es incorrecta")
    else:
        sexo = int(input("1. Hombre\n 2. Mujer \nSelecciona una opcion: "))
        if sexo == 1:
            estado_civil = int(input("1. Casado\n 2. Soltero \nSelecciona una opcion: "))
            if estado_civil == 1:
                HCasados += 1
            elif estado_civil == 2:
                HSolteros += 1
            else:
                print("La opcion ingresada es incorrecta")
        elif sexo == 2:
            estado_civil = int(input("1. Casado\n 2. Soltero \nSelecciona una opcion: "))
            if estado_civil == 1:
                MCasadas += 1
            elif estado_civil == 2:
                MSolteras += 1
            else:
                print("La opcion ingresada es incorrecta")
        else:
            print("La opcion ingresada es incorrecta")

print(f"En la ciudad de Medellin hay {HCasados} hombres casados")
print(f"En la ciudad de Medellin hay {MCasadas} mujeres casadas")
print(f"En la ciudad de Medellin hay {HSolteros} hombres solteros")
print(f"En la ciudad de Medellin hay {MSolteras} mujeres solteras")
print(f"Las personas menores de edad o con datos incorrectos son: {Menores}")