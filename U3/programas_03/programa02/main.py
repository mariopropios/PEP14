"""
Modifica el programa principal (main,py) del ejercicio anterior para que siga la siguiente
estructura.
"""

import operaciones

# Definicion de funciones principales
def main():
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))

    print("Suma:            ", operaciones.suma(a, b))
    print("Resta:           ", operaciones.resta(a, b))
    print("Multiplicacion:  ", operaciones.multiplicacion(a, b))
    print("Division:        ", operaciones.division(a, b))
    
# Bloqueo: solo se ejecuta si este archivo es el principal
if __name__ == "__main__":
    # Aqui se puede inicializar o procesar argumentos
    main()