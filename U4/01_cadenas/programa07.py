"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Declara una cadena " Hola Mundo ".
     Aplica y muestra los resultados de: upper(), lower(), capitalize(),
    title().
     Elimina espacios con strip().
     Sustituye "Mundo" por "Python" con replace().
     Divide la cadena en palabras con split().
     Une una lista de palabras con join().
"""
cadena = " Hola Mundo "

print("upper:", repr(cadena.upper()))

print("lower:", repr(cadena.lower()))

print("capitalize:", repr(cadena.capitalize()))

print("title:", repr(cadena.title()))

print("strip:", repr(cadena.strip()))

print("replace:", repr(cadena.replace("Mundo", "Python")))

palabras = cadena.split()
print("split:", palabras)

lista = ["@", "mario", "propios", "plaza"]
print("join:", " ".join(lista))