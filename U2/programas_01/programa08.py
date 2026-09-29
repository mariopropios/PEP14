import random

# Jugador 1
dado1 = random.randrange(1, 7)
dado2 = random.randrange(1, 7)

# Jugador 2
dado3 = random.randrange(1, 7)
dado4 = random.randrange(1, 7)

print("Jugador 1 ha sacado:", dado1, "y", dado2)
print("Jugador 2 ha sacado:", dado3, "y", dado4)

sumaj1 = dado1 + dado2
sumaj2 = dado3 + dado4

dadoAlto1 = max(dado1, dado2)
dadoAlto2 = max(dado3, dado4)

if sumaj1 > sumaj2:
    print("Gana el jugador 1 con", sumaj1)
elif sumaj1 < sumaj2:
    print("Gana el jugador 2 con", sumaj2)
else:
    if dadoAlto1 > dadoAlto2:
        print(
            "Empate a puntos de dado, pero gana el jugador 1 por su dado alto",
            dadoAlto1,
        )
    elif dadoAlto1 < dadoAlto2:
        print(
            "Empate a puntos de dado, pero gana el jugador 2 por su dado alto",
            dadoAlto2,
        )
    else:
        print("Empate a puntos y en dado alto")
