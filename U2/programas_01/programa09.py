import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")
num1 = int(input("Seleccione una opción:"))

num2 = random.randrange(1, 4)

if num1 == num2:
    print("EMPATE")
elif (
    (num1 == 3 and num2 == 2) or (num1 == 2 and num2 == 1) or (num1 == 1 and num2 == 3)
):
    print("Ganaste al ordenador")
else:
    print("Perdiste contra el ordenador")

print("El ordenador sacó", num2)
