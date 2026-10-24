# imports de modulos 
from matematicas import (
    a_binario,
    a_entero,
    a_hexadecimal,
    area_circulo,
    area_rectangulo,
    area_triangulo,
    division,
    multiplicacion,
    resta,
    suma,
)


# Definicion de funciones principales
def main():
    """MENU"""
    print("1. Operaciones matematicas")
    print("2. Calculo de areas geometricas")
    print("3. Conversiones")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        a = float(input("Primer numero: "))
        b = float(input("Segundo numero: "))

        print("Suma:", suma(a, b))
        print("Resta:", resta(a, b))
        print("Multiplicacion:", multiplicacion(a, b))
        print("Division:", division(a, b))

    elif opcion == 2:
        print("1. Rectangulo")
        print("2. Triangulo")
        print("3. Circulo")

        figura = int(input("Elige figura: "))
        if figura == 1:
            base = float(input("Base: "))
            altura = float(input("Altura: "))

            print("Area:", area_rectangulo(base, altura))
        elif figura == 2:
            base = float(input("Base: "))
            altura = float(input("Altura: "))

            print("Area:", area_triangulo(base, altura))
        elif figura == 3:
            radio = float(input("Radio: "))

            print("Area:", area_circulo(radio))

    elif opcion == 3:
        print("1. A binario")
        print("2. A hexadecimal")
        print("3. Texto a entero")

        conv = int(input("Elige conversion: "))
        if conv == 1:
            n = int(input("Numero entero: "))
            print("Binario:", a_binario(n))
        elif conv == 2:
            n = int(input("Numero entero: "))
            print("Hexadecimal:", a_hexadecimal(n))
        elif conv == 3:
            texto = input("Texto: ")
            print("Entero:", a_entero(texto))


if __name__ == "__main__":
    main()