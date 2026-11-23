from cocina.chef import preparar_plato, mostrar_chef
from cocina.rival import generar_rival, preparar_plato_rival, mostrar_rival


def main():
    print("===  DUELO DE COCINA  ===")

    try:
        nombre = input("Introduce tu nombre: ").strip()

        tecnica = int(input("Técnica (1-10): "))
        while tecnica < 1 or tecnica > 10:
            print("Debe estar entre 1 y 10.")
            tecnica = int(input("Técnica (1-10): "))

        energia = int(input("Energía inicial (1-5): "))
        while energia < 1 or energia > 5:
            print("Debe estar entre 1 y 5.")
            energia = int(input("Energía inicial (1-5): "))
    except ValueError:
        print("Error: introduce números válidos.")
        return

    nombre_rival, tec_rival, energia_rival = generar_rival()

    mostrar_chef(nombre, tecnica, energia)
    mostrar_rival(nombre_rival, tec_rival, energia_rival)

    for ronda in range(1, 4):
        print(f"\n--- RONDA {ronda} ---")

        plato_chef = preparar_plato(tecnica, energia)
        plato_rival = preparar_plato_rival(tec_rival, energia_rival)

        print(f"Plato de {nombre}: {plato_chef}")
        print(f"Plato de {nombre_rival}: {plato_rival}")

        if plato_chef > plato_rival:
            energia_rival = energia_rival - 1
            print(f"{nombre} enamora al jurado! (-1 energía rival)")
        elif plato_rival > plato_chef:
            energia = energia - 1
            print(f"{nombre_rival} impresiona al jurado! (-1 energía chef)")
        else:
            print("Empate. Nadie pierde energía.")

    print("\n=== FIN DEL DUELO ===")
    if energia > energia_rival:
        print(f"¡{nombre} ha vencido a {nombre_rival}!")
    elif energia_rival > energia:
        print(f"¡{nombre_rival} ha vencido a {nombre}!")
    else:
        print("¡Empate!")


if __name__ == "__main__":
    main()
