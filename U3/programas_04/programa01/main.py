# imports de la libreria estandar

# imports de librerias de terceros

# imports de modulos propios
from matematicas import operaciones
from matematicas import figuras
from matematicas import conversiones



def main():
    """VISUALIZAMOS MENU"""

    print("1. Operaciones matematicas")
    print("2. Calculo de areas geometricas")
    print("3. Conversiones")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        a = float(input("Primer numero: "))
        b = float(input("Segundo numero: "))

        print("Suma:", operaciones.suma(a, b))
        print("Resta:", operaciones.resta(a, b))
        print("Multiplicacion:", operaciones.multiplicacion(a, b))
        print("Division:", operaciones.division(a, b))

    elif opcion == 2:
        print("1. Rectangulo")
        print("2. Triangulo")
        print("3. Circulo")

        figura = int(input("Elige figura: "))

        if figura == 1:
            base = float(input("Base: "))
            altura = float(input("Altura: "))

            print("Area:", figuras.area_rectangulo(base, altura))
        elif figura == 2:
            base = float(input("Base: "))
            altura = float(input("Altura: "))

            print("Area:", figuras.area_triangulo(base, altura))
        elif figura == 3:
            radio = float(input("Radio: "))

            print("Area:", figuras.area_circulo(radio))

    elif opcion == 3:
        print("1. A binario")
        print("2. A hexadecimal")
        print("3. Texto a entero")
        
        conv = int(input("Elige conversion: "))

        if conv == 1:
            n = int(input("Numero entero: "))
            print("Binario:", conversiones.a_binario(n))
        elif conv == 2:
            n = int(input("Numero entero: "))
            print("Hexadecimal:", conversiones.a_hexadecimal(n))
        elif conv == 3:
            texto = input("Texto: ")
            print("Entero:", conversiones.a_entero(texto))


# Main
if __name__ == "__main__":
    main()