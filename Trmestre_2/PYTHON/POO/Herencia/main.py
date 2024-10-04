from Empleado import Empleado
from Asesor import Asesor

correo = input("Digite el correo: ")
direccion = input("Digite el direccion: ")
apellido = input("Digite el apellido: ")
telefono = input("Digite el telefono: ")
#celular = input("Digite el celular: ")
#nombre = input("Digite el nombre: ")

#empleado = Empleado()

#empleado.obtener_datos(correo, direccion, apellido, telefono, celular, nombre)
#empleado.__str__()

asesor = Asesor()

asesor.obtener_datos(correo, direccion, apellido, telefono)
asesor.__str__()