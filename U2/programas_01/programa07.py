"""
Escriba un programa que pida un año y que escriba si es bisiesto o no. Un año es bisiesto
si es múltiplos de 4 pero no múltiplos de 100, aunque si los múltiplos de 400.
"""

anio = int(input("Introduce un año: "))

if anio % 400 == 0:
    print(anio, "es bisiesto")
elif anio % 100 == 0:
    print(anio, "no es bisiesto")
elif anio % 4 == 0:
    print(anio, "es bisiesto")
else:
    print(anio, "no es bisiesto")
