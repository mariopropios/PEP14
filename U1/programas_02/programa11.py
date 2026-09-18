horas_salida = int(input("Introduce la hora de salida (HH): "))
minutos_salida = int(input("Introduce los minutos de salida (MM): "))
segundos_salida = int(input("Introduce los segundos de salida (SS): "))
duracion_viaje = int(input("Introduce la duracion del viaje en segundos (N): "))

segundos_totales = (
    horas_salida * 3600 + minutos_salida * 60 + segundos_salida + duracion_viaje
)

# Si se pasa de las 24 horas, damos la vuelta al reloj (86400 segundos = 1 dia)
segundos_totales = segundos_totales % 86400

horas_llegada = segundos_totales // 3600
minutos_llegada = (segundos_totales % 3600) // 60
segundos_llegada = segundos_totales % 60

print(
    "La hora de llegada es:", horas_llegada, ":", minutos_llegada, ":", segundos_llegada
)
