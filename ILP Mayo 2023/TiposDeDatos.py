# Tipos de Datos: Clasificación de los datos
import datetime

# Declarar las variables
nombre = 'Eduardo'
edad = 31
estatura = 1.70
dirección = "Calle X, Mun. Y, C.P. Z"
teléfono = "5523235261"
estatus = True # True / False
colores_favoritos = ["rojo", "amarillo", "azúl"] # lista o arreglo
fecha_nacimiento = datetime.date(1991, 5, 1)

# SALIDA DE DATOS
print("Nombre: ", type(nombre))
print("Edad: ", type(edad))
print("Estatura: ", type(estatura))
print("Dirección: ", type(dirección))
print(type(teléfono))
print(type(estatus))
print(type(colores_favoritos))
print("Fecha de Nacimiento: ", fecha_nacimiento, type(fecha_nacimiento))
