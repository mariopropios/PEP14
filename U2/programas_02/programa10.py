"""
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""

import random

# La banca saca su jugada UNA sola vez
banca = random.randrange(17, 22)


jugadores = int(input("¿Cuántos jugadores van a jugar? "))

# Repetimos el turno una vez por cada jugador
for jugador in range(1, jugadores + 1):

    print(f"\n--- Turno del jugador {jugador} ---")

    # variables que se reinician por jugador
    puntos = 0
    seguir = "s"

    # lógica del juego
    while seguir == "s" and puntos <= 21:
        carta = random.randrange(1, 6)
        puntos += carta
        print(f"Has sacado un {carta}. Llevas {puntos} puntos.")

        if puntos <= 21:
            seguir = input("¿Quieres otra carta? (s/n): ").lower()

    # Resultado de ESTE jugador
    if puntos > 21:
        print(f"Jugador {jugador}: te has pasado con {puntos}. ¡Pierdes!")
    elif puntos > banca:
        print(f"Jugador {jugador}: tienes {puntos}. ¡Has ganado a la banca!")
    else:
        print(f"Jugador {jugador}: tienes {puntos}. Has perdido contra la banca.")

# Al final de la partida revelamos la puntuación de la banca
print(f"\nLa banca tenía {banca} puntos.")
