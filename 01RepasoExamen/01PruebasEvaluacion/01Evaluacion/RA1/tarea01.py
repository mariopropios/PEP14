"""
El siguiente programa pretende convertir una cantidad de minutos introducida por el usuario en
horas y minutos, mostrando el resultado con un formato legible. Sin embargo, contiene varios
errores de sintaxis y de tipo.
Corrige el código y haz que funcione correctamente. No se permite usar ninguna sentencia
condicional (if, elif, else) ni estructuras de datos. El programa debe funcionar con cualquier
cantidad entera de minutos.
"""
minutos = int(input("Introduce una cantidad de minutos: "))

horas = minutos // 60   # division entera
resto = minutos % 60    # minutos que sobran

print(f"Equivale a {horas}  horas y {resto} minutos")