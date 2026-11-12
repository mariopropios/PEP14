"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Convierte un número entero, un número decimal y un booleano en cadenas
    (str()).
     Convierte una cadena en entero y en decimal (int(), float()).
     Crea una cadena cruda (r"...") que contenga caracteres especiales y muéstrala.
"""

entero = 42
decimal = 3.14
booleano = True

texto_entero = str(entero)
texto_decimal = str(decimal)
texto_booleano = str(booleano)

print(texto_entero, type(texto_entero))
print(texto_decimal, type(texto_decimal))
print(texto_booleano, type(texto_booleano))

numero_entero = int("100")
numero_decimal = float("2.5")

print(numero_entero + 1, type(numero_entero))
print(numero_decimal * 2, type(numero_decimal))

ruta_normal = "C:\nueva\tabla"
ruta_cruda = r"C:\nueva\tabla"

print("Normal:", ruta_normal)
print("Cruda:", ruta_cruda)