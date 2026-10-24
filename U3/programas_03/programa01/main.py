"""
Crea un módulo llamado operaciones que contenga cuatro funciones básicas
relacionadas con operaciones numéricas:
     suma(a, b) → devuelve la suma de dos números.
     resta(a, b) → devuelve la resta de dos números.
     multiplicacion(a, b) → devuelve la multiplicación de dos números.
     division(a, b) → devuelve la división de dos números (controlando la división entre
    cero).
Crea un programa principal main.py que y importe el módulo matemáticas, pida al usuario
dos números y muestre los resultados de aplicar cada una de las funciones anteriores.
"""

import operaciones

# Clase leer número
def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Eso no es un numero. Intentalo de nuevo.")


# Pedir datos
a = leer_numero("Primer numero: ")
b = leer_numero("Segundo numero: ")

# Visualizar
print("Suma:            ", operaciones.suma(a, b))
print("Resta:           ", operaciones.resta(a, b))
print("Multiplicacion:  ", operaciones.multiplicacion(a, b))
print("Division:        ", operaciones.division(a, b))