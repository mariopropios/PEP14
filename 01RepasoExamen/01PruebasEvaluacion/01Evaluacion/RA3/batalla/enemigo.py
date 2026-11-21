"""
enemigo: tendrá las siguientes funciones:
◦ generar_enemigo(): genera aleatoriamente los atributos del enemigo (nombre,
conocimiento – entre 1 y 10 - , energía – entre 1 y 5- ) y los devuelve.
    ▪ Para generar el nombre puedes usar el siguiente código
    nombres = ["Hydra", "Kraken", "Minotauro", "Gorgona", "Titán"]
    nombre = random.choice(nombres)
◦ ataque_enemigo(conocimiento, energía): devuelve el nivel de magia del enemigo,
calculado de igual forma conocimiento * energía) * número aleatorio entre 1 y 3.
◦ mostrar_enemigo(nombre, conocimiento, energía): muestra en pantalla los valores
actuales del enemigo.
"""
import random

def generar_enemigo():
    nombres = ["Hydra", "Kraken", "Minotauro", "Gorgona", "Titán"]
    nombre = random.choice(nombres)
    conocimiento = random.randint(1,10)
    energia = random.randint(1,5)
    return nombre, conocimiento, energia

def ataque_enemigo(conocimiento,energia):
    return conocimiento * energia * random.randint(1,3)

def mostrar_enemigo(nombre, conocimiento, energia):
    print(f"\nEnemigo: {nombre}")
    print(f"    Conocimiento: {conocimiento}")
    print(f"    Energía: {energia}")