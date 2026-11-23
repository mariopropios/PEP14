import random


def generar_evento(energia):

    numero_aleatorio = random.randint(1, 5)

    if energia < 10:
        if numero_aleatorio == 2 or numero_aleatorio == 3:
            return 2
        elif numero_aleatorio == 4 or numero_aleatorio == 5:
            return 3
        else:
            return numero_aleatorio
    else:
        if numero_aleatorio == 1 or numero_aleatorio == 2 or numero_aleatorio == 3:
            return 1
        elif numero_aleatorio == 4:
            return 2
        else:
            return 3


def valor_tesoro(energia):
    return energia + random.randint(1, 5)
