"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Declara variables con tu nombre, curso y año.
     Muestra un mensaje con str.format().
     Muestra el mismo mensaje usando f-strings.
     Usa un f-string para mostrar el resultado de una operación matemática con dos
    números.
"""
nombre = "Mario"
curso = "2º DAW"
anio = 2026

print("Me llamo {}, estudio {} y estamos en {}.".format(nombre, curso, anio))

print(f"Me llamo {nombre}, estudio {curso} y estamos en {anio}.")

a = 7
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} / {b} = {a / b:.2f}")