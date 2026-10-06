"""
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
"""

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el día: "))
annio = int(input("Introduce el año: "))


if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    diasTotalesMes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    diasTotalesMes = 30
elif mes == 2:
    # Bisiestos
    if (annio % 4 == 0 and annio % 100 != 0) or (annio % 400 == 0):
        diasTotalesMes = 29
    else:
        diasTotalesMes = 28

if 1 <= mes <= 12 and 1 <= dia <= diasTotalesMes:
    print("La fecha que has introducido es correcta")
else:
    print("Error. La fecha que has introducido es incorrecta")
