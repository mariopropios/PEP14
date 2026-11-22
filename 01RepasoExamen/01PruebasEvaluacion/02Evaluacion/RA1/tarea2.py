"""
Crea un programa en Python que pida datos al usuario y realice comprobaciones.
No se puede usar ninguna estructura condicional (if, elif, else) ni estructuras de datos.

El programa debe:
    Pedir: un número entero (edad), un número decimal (altura en metros) y una cadena (nombre), convirtiendo cada valor al tipo correspondiente.
    Mostrar el valor y el tipo de cada variable.
    Comprobar que cada variable es del tipo correcto y guardar el resultado en variables booleanas.
    Mostrar si todas las comprobaciones son correctas o no.
    Si todas son correctas, mostrar un mensaje con el nombre y el resultado de edad * altura.
    Si alguna no lo es, mostrar un mensaje de error.
    Sin usar if / elif / else.
"""

# --- PEDIR DATOS
edad = int(input("Introduce una edad: "))
altura = float(input("Introduce una altura: "))
nombre = str(input("Introduce un nombre: "))

# --- MOSTRAR VALOR Y TIPO
print(f"Edad: {edad} es {type(edad)} ")
print(f"Altura: {altura} es {type(altura)} ")
print(f"Nombre: {nombre} es {type(nombre)} ")

# --- COMPROBACIONES BOOLEANAS
es_entero = type(edad) is int
es_decimal = type(altura) is float
es_texto = type(nombre) is str

# --- SI TODAS SON CORRECTAS MOSTRARLO
todas_correctas = (es_entero and es_decimal and es_texto)
print(f"¿Son todas correctas? {todas_correctas}")

# --- MENSAJE CORRECTAS E INCORRECTAS
mensaje = (todas_correctas * f"{nombre}: edad * altura = {edad * altura}" +
           (not todas_correctas) * "Error, no son todas correctas")
print(mensaje)
