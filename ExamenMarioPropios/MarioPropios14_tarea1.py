nombre = str(input("Introduce el nombre del conductor: "))
kilometros = float(input("Introduce los kilometros recorridos: "))
ocupantes = int(input("Número de ocupantes del vehículo: "))

CONSUMO_100KM = 6.5
PRECIO_LITRO = 1.60
DESCUENTO = 10


litros = kilometros * CONSUMO_100KM

coste = litros * PRECIO_LITRO

coste_total = coste * (DESCUENTO / 100)

coste_ocupante = coste_total / ocupantes


# MOSTRAR VALOR Y TIPO DE DATO
print(f"{nombre} es ", type(nombre))
print(f"{kilometros} es ", type(kilometros))
print(f"{ocupantes} es ", type(ocupantes))

# COMPROBAR CON ISINSTANCE()
es_string = isinstance(nombre, str)
es_float = isinstance(kilometros, float)
es_int = isinstance(ocupantes, int)

todas_correctas = es_string and es_float and es_int
print(f"¿Todas son correctas? {todas_correctas}")

mensaje = (
    todas_correctas * f"{es_string} , {es_float} , {es_int}"
    + (not todas_correctas) * "No son todas correctas"
)

print(mensaje)

# VISUALIZAR RESUMEN
print(f"Nombre: {nombre}")
print(f"Kilometros: {kilometros}")
print(f"Número de ocupantes: {ocupantes}")

print(f"Combustible consumido: {litros:.2f} litros")
print(f"Coste inicial: {coste:.2f} euros")
print(f"Descuento aplicado: {(coste - coste_total):.2f} euros")
print(f"Coste total: {coste:.2f} euros")
print(f"Importe a pagar por ocupante: {coste_ocupante:.2f} euros")
