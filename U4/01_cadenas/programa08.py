"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Declara una cadena "programación en Python".
     Busca la posición de "Python" con find() o index().
     Cuenta cuántas veces aparece la letra "o".
     Verifica si comienza por "pro" y termina por "on".
"""

cadena = "programación en Python"

print("Posición con find():", cadena.find("Python"))

print("Posición con index():", cadena.index("Python"))

print("find() de algo que no existe:", cadena.find("Java"))

print("Veces que aparece 'o':", cadena.count("o"))

print("¿Empieza por 'pro'?", cadena.startswith("pro"))

print("¿Termina por 'on'?", cadena.endswith("on"))
