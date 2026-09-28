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
