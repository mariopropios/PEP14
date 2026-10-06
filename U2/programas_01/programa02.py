"""
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso.
"""

print("Introduce un número par: ")
par = int(input())

if par % 2 != 0:
    print("Error. No es par")
else:
    print("Introduce un número impar: ")
    impar = int(input())
    if impar % 2 == 0:
        print("Error. El segundo número no es impar")
    else:
        print("Correcto. Digitó los dos números correctamente")
