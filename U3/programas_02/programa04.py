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

t = turtle.Turtle()
t.pensize(3)
t.speed(3)

# 1) Cuadrado rojo sin rellenar
t.pencolor("red")
for _ in range(4): # _ por cada vuelta realiza la siguiente acción
    t.forward(100)
    t.right(90)

# 2) Apartarse sin dibujar raya
t.penup()
t.goto(180, -50)
t.pendown()

# 3) Circulo verde RELLENO
t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
t.circle(50)
t.end_fill()

t.hideturtle()
turtle.done()