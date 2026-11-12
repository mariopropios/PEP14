"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Define tres cadenas con comillas simples, dobles y triples.
     Muestra en pantalla cada una.
     Accede y muestra el primer y último carácter de una cadena mediante índices
    positivo y negativo.
"""

cadena_simple = 'Hola con comillas simples'
cadena_doble = "Hola con cadena dobele"
cadena_triple = """Hola con cadena triple,
que pueden ocupar varias lineas"""

print(cadena_simple)
print(cadena_doble)
print(cadena_triple)

print("Primer carácter (índice 0):", cadena_simple[0])
print("Último carácter (índice -1):", cadena_simple[-1])
print("Último carácter (índice positivo):", cadena_simple[len(cadena_simple) - 1])
