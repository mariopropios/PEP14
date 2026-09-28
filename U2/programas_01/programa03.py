print("Introduce un número (dividendo):")
n1 = float(input())

print("Introduce otro número (divisor)")
n2 = float(input())

try:
    resultado = n1 / n2
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print(f"El resultado es: {resultado}")
