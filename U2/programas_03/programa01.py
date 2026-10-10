"""
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente. Controla las posibles
excepciones a la hora de introducir el número por teclado.
"""

esValido = False

while(not esValido):
    try:
        numero = int(input("Introduce un número del 1 al 10: "))
        if(numero>= 1 and numero<=10):
            esValido = True
        else:
            print("El número debe de estar entre 1 y 10")
    except ValueError:
        print("Eso no es un número entero, introduce uno de nuevo")

print(f"Has introducido el número {numero}")
