"""
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos.
"""

import random

secreto = random.randrange(1, 21)

intentos = 0
acertado = False


while intentos < 3 and not acertado:
    numero = int(input("Adivina el número (1-20): "))
    intentos += 1  # gastamos un intento

    if numero == secreto:
        acertado = True  # fin while
    elif secreto > numero:
        print("El número a adivinar es MAYOR")
    else:
        print("El número a adivinar es MENOR")

# Visualizado final
if acertado:
    print(f"¡Has acertado en {intentos} intento(s)!")
else:
    print(f"Te has quedado sin intentos. El número era {secreto}")
