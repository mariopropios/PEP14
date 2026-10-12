"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
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

# Validaciones
def leerDecimalPositivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))       
            if valor > 0:
                return valor
            print("El valor debe ser mayor que 0.")
        except ValueError:
            print("Eso no es un número válido")

def leerOpcionMenu(mensaje):
    while True:
        try:
            opcion = int(input(mensaje))
            if 1 <= opcion <= 4:
                return opcion
            print("Opción no válida. Debe estar entre 1 y 4.")
        except ValueError:
            print("Eso no es un número entero. Inténtalo de nuevo.")

# Opciones
def opcion1():
    radio = leerDecimalPositivo("Introduce el radio del círculo: ")
    area = calcular_area_circulo(radio)
    print(f"El area del círculo es {area}")

def opcion2():
    base = leerDecimalPositivo("Introduce la base: ")
    altura = leerDecimalPositivo("Introduce la altura: ")
    area = calcular_area_triangulo(base, altura)
    print(f"El area del triángulo es {area}")

def opcion3():
    base = leerDecimalPositivo("Introduce la base: ")
    altura = leerDecimalPositivo("Introduce la altura: ")
    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es {area}")

#----- MAIN
def main():
    opcion = 0
    while(opcion != 4):
        mostrar_menu()
        opcion = leerOpcionMenu("Introduce una opción: ")

        if(opcion==1):
            opcion1()
        elif(opcion==2):
            opcion2()
        elif(opcion==3):
            opcion3()

# ARRANCAMOS EL PROGRAMA
main()


