numero = int(input("Introduce un numero de dos cifras: "))

decenas = numero // 10
unidades = numero % 10

numero_invertido = unidades * 10 + decenas

print("El numero invertido es:", numero_invertido)
