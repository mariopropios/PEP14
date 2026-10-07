"""
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana.
"""

import random

# Jugada de la banca: entre 17 y 21
banca = random.randrange(17, 22)

puntos = 0  # puntuación del jugador
seguir = "s"  # s: quiere otra carta


while seguir == "s" and puntos <= 21:
    carta = random.randrange(1, 6)  # carta del 1 al 5
    puntos += carta  # sumamos
    print(f"Has sacado un {carta}. Llevas {puntos} puntos.")

    if puntos <= 21:  # solo preguntamos si aún puede jugar
        seguir = input("¿Quieres otra carta? (s/n): ").lower()

# Visualizar final
print(f"Tu puntuación: {puntos} | Banca: {banca}")

if puntos > 21:
    print("Te has pasado de 21. ¡Has perdido!")
elif puntos > banca:
    print("¡Has ganado!")
else:
    print("Has perdido (igual o menor que la banca).")
