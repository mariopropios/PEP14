segundos = int(input("Introduce una cantidad de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
resto = segundos % 60

print(f"Equivale a {horas}h {minutos}m {resto}s")