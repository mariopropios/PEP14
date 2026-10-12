"""
Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
similar al siguiente:
    1. Calcular el área de un círculo
    2. Calcular el área de un triángulo
    3. Calcular el área de un rectángulo
    4. Salir
Introduce una opción (1-4):
El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
opción 4.
Hay que diseñar y definir la siguientes funciones: :
     calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y
    retorna su área.
     calcular_area_triangulo: recibe como parámetros de entrada la base y la altura
    del triangulo y retorna su área.
     calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura
    del rectángulo y retorna su área.
     mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
     main(): lee por teclado la opción seleccionada por el usuario, valida que la opción
    está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función
    correspondiente en función de la opción seleccionada.
     opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre
    sea mayor que 0 y una vez que ha validado el radio llamará a la función
    calcular_area_circulo.
     opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo,
    valida que los dos datos son mayores que 0 y una vez que los ha validado llamará
    a la función calcular_area_triangulo.
     opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que
    los dos datos son mayores que 0 y una vez que los ha validado llamará a la función
    calcular_area_rectangulo.
"""
import math

# Menú
def mostrar_menu():

    print("1. Calcular area de un círculo")
    print("2. Calcular area de un triángulo")
    print("3. Calcular area de un rectángulo")
    print("4. Salir")

# Calculos
def calcular_area_circulo(radio):
    resultado = math.pi * radio**2
    return resultado
def calcular_area_triangulo(base,altura):
    resultado = (base*altura)/2
    return resultado
def calcular_area_rectangulo(base,altura):
    resultado = base*altura
    return resultado

# Opciones
def opcion1():
    radio = float(input("Introduce el radio del círculo: "))
    while radio<=0:
        print("El radio debe ser mayor a 0")
        radio = float(input("Introduce el radio del círculo: "))
    area = calcular_area_circulo(radio)
    print(f"El area del círculo es {area}")

def opcion2():
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    while base <= 0 or altura <= 0:
        print("La base y la altura deben ser mayores que 0.")
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
    area = calcular_area_triangulo(base, altura)
    print(f"El area del triángulo es {area}")

def opcion3():
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    while base <= 0 or altura <= 0:
        print("La base y la altura deben ser mayores que 0.")
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es {area}")

#----- MAIN
def main():
    opcion = 0
    while(opcion != 4):
        mostrar_menu()
        opcion = int(input("Introduce una opción: "))

        # validamos la opción
        while(opcion<1 or opcion>4):
            print("Opción no valida")
            opcion = int(input("Introduce una opción: "))

        if(opcion==1):
            opcion1()
        elif(opcion==2):
            opcion2()
        elif(opcion==3):
            opcion3()

# ARRANCAMOS EL PROGRAMA
main()


