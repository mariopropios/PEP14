"""
Escribe un programa en Python que importe el modulo math completo y que le pregunte al
usuario que operación matemática quiere hacer:
    1. Seno de un ángulo
    2. Coseno de ángulo
    3. Raíz cuadrada de un número
    4. Potencia de dos números.
Le pida los datos necesarios y muestre los resultados por pantalla.
"""
import math

# MENÚ
def menu():
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")

# CÁLCULOS
def seno(angulo):
    return math.sin(math.radians(angulo))

def coseno(angulo):
    return math.cos(math.radians(angulo))

def raizCuadrada(numero):
    return math.sqrt

def potencia(base,exponente):
    return math.pow(base,exponente)

# VALIDACIÓN LECTURA
def leerDecimalPositivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))       
            if valor > 0:
                return valor
            print("El valor debe ser mayor que 0.")
        except ValueError:
            print("Eso no es un número válido")

def leerOpcionMenu():
    while True:
        try:
            opcion = int(input("Introduce una opción: "))
            if 1 <= opcion <= 4:
                return opcion
            print("Opción no válida. Debe estar entre 1 y 4.")
        except ValueError:
            print("Eso no es un número entero. Inténtalo de nuevo.")

# PROGRAMA 
def main():
    menu()
    opcion = leerOpcionMenu()

    if opcion == 1:
        angulo = leerDecimalPositivo("Introduce el ángulo en grados: ")
        print(f"El seno de {angulo}° es {seno(angulo)}")

    elif opcion == 2:
        angulo = leerDecimalPositivo("Introduce el ángulo en grados: ")
        print(f"El coseno de {angulo}° es {coseno(angulo)}")

    elif opcion == 3:
        numero = leerDecimalPositivo("Introduce un número: ")
        while numero < 0:                      
            print("No se puede calcular la raíz de un número negativo.")
            numero = leerDecimalPositivo("Introduce un número: ")
        print(f"La raíz cuadrada de {numero} es {raizCuadrada(numero):.2f}")

    else: # opción 4
        base = leerDecimalPositivo("Introduce la base: ")
        exponente = leerDecimalPositivo("Introduce el exponente: ")
        print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")

main()