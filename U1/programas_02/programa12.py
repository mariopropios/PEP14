millas = float(input("Introduce un numero de millas: "))
kilometros = float(input("Introduce un numero de kilometros: "))

millasKm = round(millas * 1.61, 2)
kmMillas = round(kilometros / 1.61, 2)

print(millas, "millas son", millasKm, "kilometros")
print(kilometros, "kilometros son", kmMillas, "millas")
