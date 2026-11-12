"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Crea una cadena que incluya saltos de línea y tabuladores usando \n y \t.
     Divide una cadena larga en varias líneas sin perder legibilidad.
     Muestra el resultado en pantalla
"""
tabla = "Nombre\tCurso\tNota\nMario\t2DAW\t9\nLaura\t2DAW\t8"

print(tabla)

texto_largo = (
    "Esta es una cadena muy larga que se ha dividido "
    "en varias líneas dentro del código para que sea "
    "más fácil de leer, pero al mostrarla sale seguida."
)

print(f"\n{texto_largo}")