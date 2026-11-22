import random

fichas = 5
victorias = 0
racha = 0
racha_maxima = 0

while (fichas > 0):
    print("\nJugador")
    print(f"    -Fichas:{fichas}")
    print(f"    -Victorias:{victorias}")
    
    try:
    
        estrategia = input("\nElige estrategia (seguro/normal/allin): ").strip().lower()
        
        if(estrategia == "seguro"):
            jugador = random.randint(2,6)
            casa = random.randint(3,7)
        elif(estrategia == "normal"):
            jugador = random.randint(1,8)
            casa = random.randint(1,8)
        elif(estrategia == "allin"):
            jugador = random.randint(1,12)
            casa = random.randint(4,10)
        else:
            print("Error. Esa estrategia no es valida")
            continue

        print(f"\nTu dado: {jugador}")
        print(f"Dado de la casa: {casa}")

        if(jugador>casa):
            victorias += 1
            print("\nGanaste")
            racha += 1
            if (racha>racha_maxima):
                racha_maxima = racha

            if(racha == 3):
                if(fichas < 5):
                    fichas = fichas + 1
                    print("Racha de 3, recuperas 1 punto")
                else:
                    print("Racha de 3, fichas ya al máximo")
                racha = 0 
        elif(jugador<casa):
            fichas -= 1
            racha = 0
            print("\nPerdiste")
        else:
            print("\nEmpate")

    except Exception:
            print("Error en la entrada")

# VISUALIZACION FINAL
print("\n--- FIN DE BATALLA ---")
print(f"Victorias: {victorias}")
print(f"Máximo de rachas: {racha_maxima}")