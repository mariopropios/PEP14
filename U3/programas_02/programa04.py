"""
El módulo turtle es una biblioteca estándar de Python que permite crear gráficos y dibujos
de manera sencilla, moviendo una “tortuga” virtual por la pantalla. El módulo está instalado
por defecto en el interprete de Python.
Investiga la documentación del módulo https://docs.python.org/3/library/turtle.html y
escribe un programa que:
     Dibuje un cuadrado rojo sin rellenar.
     Dibuje un circulo verde relleno.
"""
import turtle

# Ventana
pantalla = turtle.Screen()
pantalla.title("programa04 - turtle")
pantalla.bgcolor("white")

t = turtle.Turtle()  # crea el boli que se mueve
t.pensize(3)         # grosor de la raya (3 pixeles)
t.speed(3)           # velocidad de dibujo (1 lento, 10 rapido)

# --- 1) Cuadrado rojo SIN rellenar 
t.pencolor("red")    # el trazo sera rojo
for _ in range(4):   # repite 4 veces (4 lados) _ = no usamos el numero de vuelta
    t.forward(100)   # avanza 100 pixeles (dibuja un lado)
    t.right(90)      # gira 90 grados a la derecha (esquina)

# --- 2) Moverse sin dejar raya 
t.penup()            # levanta el boli, se puede mover sin dibujar
t.goto(180, -50)     # salta a otra posicion (x=180, y=-50) para no tapar el cuadrado
t.pendown()          # baja el boli, a partir de aqui vuelve a dibujar

# --- 3) Circulo verde RELLENO 
t.pencolor("green")  # trazo verde
t.fillcolor("green") # relleno verde
t.begin_fill()       # "desde aqui empieza la forma a rellenar"
t.circle(50)         # dibuja un circulo de radio 50
t.end_fill()         # cierra la forma y pinta el interior de verde
t.hideturtle()       # esconde la flecha/tortuga al terminar
turtle.done() 