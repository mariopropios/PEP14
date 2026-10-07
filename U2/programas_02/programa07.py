"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no.
"""

# -----CON BREAK
suma = 0
cantidad = 0

while True:
    numero = int(input("Introduce un número (0 para terminar): "))

    if numero == 0:
        break  # el cero corta el bucle

    suma += numero
    cantidad += 1

# Aquí ya hemos salido del bucle
if cantidad > 0:
    media = suma / cantidad
    print(f"La suma es {suma}")
    print(f"La media es {media}")
else:
    print("No has introducido ningún número")

# ----SIN BREAK
suma = 0
cantidad = 0

numero = int(input("Introduce un número (0 para terminar): "))

while numero != 0:
    suma += numero
    cantidad += 1
    # Pedimos el siguiente (al final de la vuelta)
    numero = int(input("Introduce un número (0 para terminar): "))

if cantidad > 0:
    media = suma / cantidad
    print(f"La suma es {suma}")
    print(f"La media es {media}")
else:
    print("No has introducido ningún número")
