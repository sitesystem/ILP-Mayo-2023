# EJEMPLO 2. Operaciones Matemáticas:
# Suma, Resta, Mult, Div, Potencia, Raíz, Módulo

# Importar una librería de funciones matemáticas
import math

# ENTRADAS DE DATOS
# Declarar o crear las VARIABLES
# SINTAXIS:
número_1 = float(input("Escribe el 1er número: "))
número_2 = float(input("Escribe el 2do número: "))

# PROCESOS (Operaciones o cálculos matemáticos y/o lógicos)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicación = número_1 * número_2
división = número_1 / número_2

potencia_1 = número_1 ** número_2	
potencia_2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = 20 % 6

# SALIDA DE DATOS
print("La suma es =", suma)
print("La suma es = " + str(suma)) # CONCATENACIÓN (Unión de 2 o más textos)
# CASTEO (Convertir un tipo de dato en otro tipo de dato)
print(f"La suma es = {suma}")

print("La resta es =", round(resta, 2))
print("La multiplicación es =", round(multiplicación, 2))
print("La división es =", round(división, 2))

print("El módulo o residuo de 20%6 es =", módulo_residuo)
