"""
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue.
"""
#WHILE
contador = 0

while(contador<=10):
    if(contador % 2 == 0):
        print(f"El número {contador} es par" )

    contador += 1

#WHILE CONTINUE (salta)
contador = 0

while contador <= 10:
    if contador % 2 != 0:        # Impar
        contador += 1            
        continue                 # Saltamos a la siguiente vuelta
    print(f"El número {contador} es par")   # aquí solo llegan los pares
    contador += 1

#FOR
for numero in range(0,11):
    if (numero % 2 == 0):
        print(f"El número {numero} es par")

#FOR CONTINUE (salta)
for numero in range(0,11):
    if (numero % 2 != 0):
        continue
    print(f"El número {numero} es par")