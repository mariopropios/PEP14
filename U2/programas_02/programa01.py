"""
Escribe un programa que muestre una lista de números del 1 al 10. Resuelve el ejercicio
de dos formas distintas, utilizando los bucles for y while. Cuando utilices el bucle for
puedes hacer uso de la función range
"""

print("Bucle For")

for numero in range(1, 11):
    print(numero)

print("While")

contador = 1

while contador <= 10:
    print(contador)
    contador = contador + 1
