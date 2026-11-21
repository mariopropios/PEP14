"""
jugador: tendrá las siguientes funciones.
    ◦ ataque_jugador (conocimiento, energía): devuelve el nivel de magia del jugador,
    calculado como (conocimiento * energía) * número aleatorio entre 1 y 3.
    ◦ mostrar_jugador(nombre, conocimiento, energía): muestra en pantalla los valores
    actuales del jugador.
"""
import random

def ataque_jugador(conocimiento,energia):
    return conocimiento * energia * random.randint(1,3)

def mostrar_jugador(nombre,conocimiento,energia):
    print(f"\nJugador: {nombre}")
    print(f"    Conocimiento: {conocimiento}")
    print(f"    Energía: {energia}")