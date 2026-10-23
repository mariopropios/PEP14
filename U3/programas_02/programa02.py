"""
Modifica el programa anterior para que solo se importen las funciones del módulo math
que se usan en el programa.
"""
from math import sin, cos, radians, sqrt, pow

# MENÚ
def menu():
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")

# CÁLCULOS
def seno(angulo):
    return sin(radians(angulo))

def coseno(angulo):
    return cos(radians(angulo))

def raizCuadrada(numero):
    return sqrt(numero)

def potencia(base,exponente):
    return pow(base,exponente)

# VALIDACIÓN LECTURA
def leerOpcionMenu():
    while True:
        try:
            opcion = int(input("Introduce una opción: "))
            if 1 <= opcion <= 4:
                return opcion
            print("Opción no válida. Debe estar entre 1 y 4.")
        except ValueError:
            print("Eso no es un número entero. Inténtalo de nuevo.")

def leerNumero(mensaje):
    """Pide un número decimal cualquiera (positivo, negativo o cero)."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Eso no es un número válido")

def leerNumeroNoNegativo(mensaje):
    """Pide un número decimal mayor o igual que 0 (para la raíz)."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            print("El valor no puede ser negativo.")
        except ValueError:
            print("Eso no es un número válido")
# PROGRAMA 
def main():
    menu()
    opcion = leerOpcionMenu()

    if opcion == 1:
        angulo = leerNumero("Introduce el ángulo en grados: ")
        print(f"El seno de {angulo}° es {seno(angulo):2f}")

    elif opcion == 2:
        angulo = leerNumero("Introduce el ángulo en grados: ")
        print(f"El coseno de {angulo}° es {coseno(angulo):.4f}")

    elif opcion == 3:
        numero = leerNumeroNoNegativo("Introduce un número: ")
        print(f"La raíz cuadrada de {numero} es {raizCuadrada(numero):.4f}")

    else:  # opción 4
        base = leerNumero("Introduce la base: ")
        exponente = leerNumero("Introduce el exponente: ")
        try:
            print(f"{base} elevado a {exponente} es {potencia(base, exponente):.4f}")
        except (ValueError):
            print("No se puede calcular esa potencia.")

# ARRANCAR PROGRAMA
main()