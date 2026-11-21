"""
Crea un programa principal main.py que (debe cumplir con la plantilla recomendada).
    • Pide al jugador su nombre, conocimiento (valor entre 1 y 10) y energía inicial (valor entre 1
    y 5).
    • Genera un enemigo aleatorio.
    • Realiza un combate de 3 rondas con el siguiente funcionamiento:
        ◦ Cada ronda ambos atacan (se calcula su nivel de magia).
        ◦ El que tenga menor nivel pierde 1 punto de energía. Si empatan ninguno pierde
        energía.
        ◦ Se muestra el resultado de la ronda.
    • Al final, se muestra quién gana (el que tenga más energía) o si hay empate.
"""
from batalla.jugador import ataque_jugador, mostrar_jugador
from batalla.enemigo import generar_enemigo, ataque_enemigo, mostrar_enemigo

def main():
    print("--- BATALLA DE MAGIA ---")

    # NOMBRE
    nombre = input("Introduce tu nombre: ").strip()

    # CONOCIMIENTO
    conocimiento = int(input("Nivel de conocimiento (1-10): "))
    while conocimiento < 1 or conocimiento > 10:
        print("Debe estar comprendido entre 1 y 10: ")
        conocimiento = int(input("Nivel de conocimiento (1-10): "))

    # ENERGÍA
    energia = int(input("Energía inicial (1-5): "))
    while energia < 1 or energia > 5:
            print("Debe estar comprendido entre 1 y 5: ")
            conocimiento = int(input("Energía inicial (1-5): "))

    # GENERAMOS ENEMIGO
    nombre_enemigo, conocimiento_enemigo, energia_enemigo = generar_enemigo()

    # VISUALIZAMOS LOS 2 JUGADORES
    mostrar_jugador(nombre,conocimiento,energia)
    mostrar_enemigo(nombre_enemigo, conocimiento_enemigo, energia_enemigo)

    # RONDAS JUGADOR
    for ronda in range(1,4):
        print(f"\n-- RONDA {ronda} --")

        magia_jugador = ataque_jugador(conocimiento,energia)
        magia_enemigo = ataque_enemigo(conocimiento_enemigo,energia_enemigo)

        print(f"Magia de {nombre}: {magia_jugador}")
        print(f"Magia de {nombre_enemigo}: {magia_enemigo}")

        if magia_jugador > magia_enemigo:
            energia_enemigo = energia_enemigo - 1
            print(f"{nombre} lanza un hechizo poderoso! (-1 energía enemigo)")
        elif magia_enemigo > magia_jugador:
            energia = energia - 1
            print(f"{nombre_enemigo} responde con un conjuro devastador! (-1 energía jugador)")
        else:
            print("Empate de magia. Nadie pierde energía.")

    #FIN DEL JUEGO
    print("\n--- FIN DEL JUEGO ---")
    if energia > energia_enemigo:
        print(f"¡{nombre} ha vencido a {nombre_enemigo}!")
    elif energia_enemigo > energia:
        print(f"¡{nombre_enemigo} ha vencido a {nombre}!")
    else:
        print("¡Empate!")

if __name__ == "__main__":
    main()

