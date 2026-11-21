"""
Crea un programa en Python que pida tres datos al usuario y realice comprobaciones, No se
puede usar ninguna estructura condicional (if, elif, else) ni estructuras de datos. El programa debe:
    • Pedir al usuario: un número entero, un número decimal y y una cadena de texto y convertir
    cada valor al tipo correspondiente.
    • Mostrar el valor y el tipo de cada variable.
    • Comprobar que cada variable es del tipo correcto y almacenar el resultado de las tres
    comprobaciones en variables booleanas.
    • Mostrar en pantalla un mensaje indicando si todas las comprobaciones son correctas o no,
    • Si todas son correctas, el programa debe mostrar la suma del número entero y el número
    decimal. Si alguna no lo es, debe mostrar un mensaje de error
"""
# LECTURA Y CONVERSION
numero_entero = int(input("Introduce un número entero:"))
numero_decimal = float(input("Introduce un número decimal:"))
cadena_texto = str(input("Introduce una cadena de texto:"))

# MOSTRAR VALOR Y TIPO
print(f"{numero_entero} es ", type(numero_entero))
print(f"{numero_decimal} es ", type(numero_decimal))
print(f"{cadena_texto} es ", type(cadena_texto))

# COMPROBACIONES BOOLEANAS
es_entero = type(numero_entero) is int
es_decimal = type(numero_decimal) is float
es_texto = type(cadena_texto) is str

print("¿Es int? ",es_entero)
print("¿Es float? ",es_decimal)
print("¿Es str? ",es_texto)

# ¿TODAS CORRECTAS?
todas_correctas = es_entero and es_texto and es_decimal
print(f"¿Todas son correctas? {todas_correctas}")

# SUMA
mensaje = (todas_correctas * f"{numero_entero + numero_decimal}" + 
           (not todas_correctas) * "Error, algo ha debido de fallar")

print(mensaje)
