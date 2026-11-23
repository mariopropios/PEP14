from exploracion.explorador import calcular_energia, calcular_puntos, mostrar_explorador
from exploracion.isla import generar_evento, valor_tesoro


def main():
    print("--- EXPLORADORES DEL TESORO ---")

    try:
        nombre = str(input("Nombre del explorador: "))

        fuerza = int(input("Fuerza (1-10): "))

        while fuerza < 1 or fuerza > 10:
            print("Debe estar entre 1 y 10.")
            fuerza = int(input("Fuerza (1-10): "))

        conocimiento = int(input("Conocimiento (1-5): "))

        while conocimiento < 1 or conocimiento > 5:
            print("Debe estar entre 1 y 5.")
            conocimiento = int(input("Energía inicial (1-5): "))
    except ValueError:
        print("Error: introduce números válidos.")
        return

    energia = calcular_energia(fuerza, conocimiento)
    energia_inicial = energia

    mostrar_explorador(nombre, energia, 0)

    for jornada in range(1, 4):
        print(f"\n--- JORNADA {jornada} ---")

        evento = generar_evento(energia)
        valor_tesoro = valor_tesoro(energia)

        if evento == 1:
            if energia >= 10:
                puntos = calcular_puntos(valor_tesoro, 5)
            else:
                puntos = calcular_puntos(valor_tesoro, 0)
        elif evento == 2:
            if energia > 0:
                energia = energia - 2
            else:
                print("La energia es 0")
        else:
            if energia_inicial > energia:
                energia = energia + 2
            else:
                print("No puede superar la energias inicial")

    print("--- FIN DE LA EXPEDICIÓN ---")
    mostrar_explorador(nombre, energia, puntos)
    if puntos >= 30:
        print("Explorador legendario")
    elif puntos >= 15 or puntos <= 29:
        print("Buena expedición")
    elif puntos < 15:
        print("Sigue explorando")
