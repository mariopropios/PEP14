"""
Escribe un programa que pida primero un número par y luego un número impar (positivos
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
impar respectivamente), se mostrará un aviso.
"""

print("Introduce un número par: ")
par = int(input())

print("Introduce un número impar: ")
impar = int(input())

if par % 2 == 0 and impar % 2 != 0:
    print("Correcto, el número par es par y el impar es impar")
else:
    print("Error. Uno de los dos números no es correcto")
