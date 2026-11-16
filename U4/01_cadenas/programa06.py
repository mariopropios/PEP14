"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Crea una cadena "Python".
     Extrae la subcadena "Pyt" con slicing.
     Extrae los caracteres en posiciones pares con slicing ::2.
     Invierte la cadena con slicing [::-1].
     Recorre la cadena carácter por carácter e imprímelos.
"""
cadena = "Python"

print("Subcadena [0:3]:", cadena[0:3])
print("Posiciones pares [::2]:", cadena[::2])
print("Invertida [::-1]:", cadena[::-1])

print("Carácter a carácter")
for caracter in cadena:
    print(caracter)
