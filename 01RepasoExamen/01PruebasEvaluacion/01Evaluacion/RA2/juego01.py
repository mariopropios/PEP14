"""
Crea un programa en Python que simule una batalla por turnos entre un jugador y un enemigo
final (el ordenador). Ambos se enfrentan lanzando cartas de poder en cada turno. El jugador
puede elegir su tipo de ataque en cada ronda, lo que afecta tanto a su carta como a la defensa del
enemigo. No se pueden usas estructuras de datos.
Reglas del juego.
    • El jugador comienza con 3 vidas y 0 puntos.
    • En cada turno:
    ◦ Se muestran las vidas del jugador.
    ◦ El jugador elige un tipo de ataque (que condiciona también la tirada del enemigo) entre:
        ▪ "fuerza": carta entre 5 y 10. El enemigo se defiende mejor (carta entre 3 y 10).
        ▪ "precisión":carta entre 3 y 8. El enemigo también estable (carta entre 2 y 9).
        ▪ "riesgo": carta entre 1 y 10. El enemigo se confunde (carta entre 1 y 8).
    ◦ Si la carta del jugador es mayor, gana el turno y suma 1 punto.
    ◦ Si la carta del enemigo es mayor, el jugador pierde una vida.
    ◦ Si las cartas son iguales, hay un empate y no se suman puntos ni se pierden vidas.
    ◦ El juego continúa mientras el jugador tenga vidas.
    ◦ Al terminar, se muestra la puntuación final
Extra: nivel del jugador
    • El jugador comienza con 3 vidas, 0 puntos y nivel 1.
    • Cada 3 puntos, el jugador sube de nivel y recupera una vida (hasta un máximo de 3).
    • Al terminar, se muestra la puntuación final y el nivel alcanzado.
"""
import random

vidas = 3
puntos = 0
nivel = 1

while(vidas>0):
    print(f"\nVidas: {vidas} | Puntos: {puntos} | Nivel: {nivel}")
    print("Elige ataque: fuerza / precision / riesgo")
    
    try:
        ataque = input("Ataque: ").strip().lower() #Quita espacios blancos y pasa a minúscula

        if (ataque == "fuerza"):
            carta_jugador = random.randint(5,10)
            carta_ordenador = random.randint(3,10)
        elif (ataque == "precision"):
            carta_jugador = random.randint(3,8)
            carta_ordenador = random.randint(2,9)
        elif (ataque == "riesgo"):
            carta_jugador = random.randint(1,10)
            carta_ordenador = random.randint(1,8)
        else:
            print("Ataque no válido. Prueba otra vez")
            continue

        print(f"Tu carta: {carta_jugador}")
        print(f"Carta Ordenador: {carta_ordenador}")

        if(carta_jugador>carta_ordenador):
            puntos += 1
            print("Ganas el turno +1 punto")
            if(puntos % 3 == 0):
                nivel += 1
                if(vidas < 3):
                    vidas += 1
                    print(f"Subes de nivel {nivel} y recuperas 1 vida")
                else:
                    print(f"Subes de nivel {nivel} y vidas ya al máximo")
        elif(carta_jugador<carta_ordenador):
            vidas -=1
            print("Pierdes el turno, -1 vida")
        else:
            print("Empate")

    except Exception:
        print("Error en la entrada de datos")

    print("FIN DE LA PARTIDA")
    print(f"Puntuación final: {puntos}")
    print(f"Nivel alcanzado: {nivel}")

