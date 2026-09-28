print("Introduce un número: ")
n1 = float(input())

print("Introduce un segundo número: ")
n2 = float(input())

if n1 > n2:
    print(f"El número {n1} es mayor que {n2}")
elif n2 > n1:
    print(f"El número {n2} es mayor que {n1}")
else:
    print(f"El número {n1} es igual a {n2}")
