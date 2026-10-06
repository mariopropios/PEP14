"""
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente.
"""

condicion = False

while condicion == False:
    numero = int(input("Digite un úmero entre el 1 y el 10: "))
    if 1 <= numero <= 10:
        condicion = True
