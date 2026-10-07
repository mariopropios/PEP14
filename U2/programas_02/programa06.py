"""
Escribe un programa que realice las siguientes operaciones:
 Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
no se introduzca el número correcto.

 Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
 Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
indica que no quiere continuar el programa finaliza.
"""

# BUCLE EXTERIOR: se repite hasta que el usuario decida parar
while True:

    # 1. pedir y validar el número
    numero = int(input("Introduce un número entre 1 y 10: "))
    while numero < 1 or numero > 10:
        print("Número no válido, inténtalo de nuevo.")
        numero = int(input("Introduce un número entre 1 y 10: "))

    # 2. mostrar la tabla de multiplicar
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):  # i va de 1 a 10
        print(f"{numero} x {i} = {numero * i}")

    # 3. preguntar si quiere continuar
    respuesta = input("¿Quieres introducir otro número? (s/n): ")
    if respuesta == "n":
        break
