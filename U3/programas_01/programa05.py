"""
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).
"""

# VARIABLE GLOBAL
variableGlobal = 15

def prueba_local():
    variableLocal = "Soy una variable local"
    print(variableLocal)
    print(f"Leo la variable global {variableGlobal}")

def prueba_asignar_sin_global():
    variableGlobal = 100 #crea esta nueva, no toca la global
    print(f"Dentro de la función variableGlobal vale {variableGlobal}")

def prueba_asignar_con_global():
    global variableGlobal
    variableGlobal = 50
    print(f"Dentro de la función variableGlobal vale {variableGlobal}")

def main():
    prueba_local()
    prueba_asignar_sin_global()
    prueba_asignar_con_global()

main()