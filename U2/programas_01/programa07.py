anio = int(input("Introduce un año: "))

if anio % 400 == 0:
    print(anio, "es bisiesto")
elif anio % 100 == 0:
    print(anio, "no es bisiesto")
elif anio % 4 == 0:
    print(anio, "es bisiesto")
else:
    print(anio, "no es bisiesto")
