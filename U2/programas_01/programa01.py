print("Introduce un número par: ")
par = int(input())

print("Introduce un número impar: ")
impar = int(input())

if par % 2 == 0 and impar % 2 != 0:
    print("Correcto, el número par es par y el impar es impar")
else:
    print("Error. Uno de los dos números no es correcto")
