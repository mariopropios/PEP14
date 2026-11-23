import random


def calcular_energia(fuerza, conocimiento):

    if fuerza <= 0 or conocimiento <= 0:
        print("fuerza y conocimiento deben ser mayores que 0")
    else:
        return fuerza + conocimiento + random.randint(1, 3)


def calcular_puntos(valor_tesoro, bonus):
    return valor_tesoro + bonus


def mostrar_explorador(nombre, energia, puntos):
    print(f"\nExplorador: {nombre}")
    print(f"    Energia: {energia}")
    print(f"    Puntos: {puntos}")
