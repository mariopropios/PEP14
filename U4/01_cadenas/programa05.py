"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Declara dos cadenas y únelas con concatenación (+).
     Repite una cadena tres veces con *.
     Compara dos cadenas lexicográficamente e indica cuál es mayor.
     Comprueba si una subcadena pertenece a otra con in.
"""

cadena1 = "manzana"
cadena2 = "pera"

union = cadena1 + " y " + cadena2

print("Concatenación:", union)

repeticion = "Ja" * 3

print("Repetición:", repeticion)

if cadena1 > cadena2:
    print(f"{cadena1} es mayor que {cadena2}")
elif cadena1 < cadena2:
    print(f"{cadena2} es mayor que {cadena1}")
else:
    print("Las dos cadenas son iguales")

subcadena = "zan"

print(f"¿{subcadena} está en {cadena1}?", subcadena in cadena1)