# ============================================================
# CHULETA PEP - sintaxis de examen (RA1 / RA2 / RA3)
# Se puede ejecutar de arriba abajo sin errores
# ============================================================

print("=== 1) ENTRADA Y SALIDA ===")
# input("texto: ")  # siempre devuelve str (comentado para que no pause)
nombre = "Mario"
edad = 20
print("hola")
print("a", "b", sep="-")
print("hola", end=" ")
print()
print(f"Hola {nombre}")
print("{} tiene {}".format(nombre, edad))

print("\n=== 2) CONVERSIONES DE TIPO ===")
x_int = int("10")
x_float = float("3.5")
x_str = str(10)
x_bool1 = bool(1)
x_bool0 = bool(0)
print(x_int, x_float, x_str, x_bool1, x_bool0)
print(type(x_int))
print(isinstance(x_int, int))

print("\n=== 3) OPERADORES ===")
a = 10
b = 3
print(a + b, a - b, a * b, a / b)  # / siempre float
print(a // b)                      # division entera
print(a % b)                       # resto
print(a ** b)                      # potencia
print(a == b, a != b, a < b, a > b, a <= b, a >= b)
print(True and False, True or False, not True)

# Truco RA1 sin if
todas_correctas = True
mensaje = todas_correctas * "Todo OK" + (not todas_correctas) * "Error"
print(mensaje)
print(todas_correctas and "Todo OK" or "Error")

print("\n=== 4) CONDICIONALES Y BUCLES ===")
numero = 2
if numero > 0:
    print("positivo")
elif numero == 0:
    print("cero")
else:
    print("negativo")

i = 0
while i < 3:
    if i == 1:
        i += 1
        continue
    print("while:", i)
    i += 1
    if i >= 3:
        break

for i in range(3):
    print("range(3):", i)

for i in range(1, 4):
    print("range(1,4):", i)

for c in "hola":
    print("char:", c)

print("\n=== 5) EXCEPCIONES ===")
try:
    n = int("abc")
except ValueError:
    print("No es un numero")
except Exception:
    print("Error general")

print("\n=== 6) FUNCIONES ===")
def nombre_funcion(param1, param2):
    """Multiplica dos valores y los devuelve."""
    resultado = param1 * param2
    return resultado

valor = nombre_funcion(2, 3)
print("nombre_funcion(2,3) =", valor)

def generar():
    return "Hydra", 8, 5

nombre_e, con, energia = generar()
print(nombre_e, con, energia)

print("\n=== 7) RANDOM Y MATH ===")
import random
import math
from math import sqrt, pi

print(random.randint(1, 10))
print(random.random())
print(random.choice(["A", "B", "C"]))
print(random.uniform(1.5, 3.5))

print(math.sqrt(9))
print(math.pow(2, 3))
print(math.floor(3.7))
print(math.ceil(3.2))
print(math.pi)
print(math.sin(0), math.cos(0))
print(sqrt(16), pi)

# Imports de paquete (solo si existe el proyecto):
# from batalla.jugador import ataque_jugador
# from batalla import ataque_jugador

print("\n=== 8) CADENAS ===")
s = "  Hola Mundo  "
print(len(s))
print(repr(s.strip()))
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.replace("Mundo", "Python"))
print(s.split())
print("usuario:root|clave:123".split("|"))
print(" ".join(["a", "b"]))
print("-".join(["a", "b"]))
print(s.find("ola"))
print(s.count("o"))
print(s.startswith("  Ho"))
print(s.endswith("o  "))
print("1540".isdigit())
print("Hola".isalpha())
print("hola".islower())
print("HOLA".isupper())
print(s[0], s[-1])
print(s.strip()[0:3])
print(s.strip()[::-1])
print("a" in s)
print("Unicode:", ord("A"), chr(65), hex(65))

print("\n=== 9) BOOLEAN / TIPOS ===")
x = 10
print(type(x) is int)
print(type(3.5) is float)
print(type("hola") is str)
print(type(True) is bool)
print(True and True)
print(False or True)
print(not False)

print("\n=== 10) VALIDACION DE RANGO ===")
valor_ok = 7
if 1 <= valor_ok <= 10:
    print("Valor en rango 1-10:", valor_ok)

print("\n=== 11) PLANTILLA MAIN ===")
def main():
    print("Aqui iria el programa principal")

if __name__ == "__main__":
    main()

# ============================================================
# ENTORNO VIRTUAL (terminal, NO Python)
# ============================================================
# python -m venv .venv
# .\.venv\Scripts\Activate.ps1
# deactivate
# python main.py
#
# __init__.py tipico:
# from .jugador import ataque_jugador, mostrar_jugador
# from .enemigo import generar_enemigo, ataque_enemigo, mostrar_enemigo