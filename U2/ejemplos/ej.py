print("Introduce tu edad")
edad = int(input())

match edad:
    case 10:
        print("Puedes ver la película")
        print("Has tenido suerte, es gratis")
    case 8:
        print("Puedes ver la película")
        print("Has tenido suerte, son 5 euros")
    case _:
        print("nddd")

if edad > 10:
    print("Puedes ver la película")
elif edad == 10:
    print("Puedes ver la película")
    print("Has tenido suerte, es gratis")
else:
    print("No puedes ver la película")

print("Adios")

print("Introduce un número")
num = int(input())

while num > 0:
    print(num)
    num = num - 1
    if num == 6:
        break
else:
    print("NO se ha complicado la condición")

# imprime de 0 a num-1 , range(3,num) eso del 3 a num-1
for i in range(num):
    print(i)

# de 0 a num-1 de 2 en dos
for i in range(0, num, 2):
    print(i)

# excepción
print("Introduce un número")
try:
    n = int(input())

    if n > 5:
        print("Hola")
    else:
        print("Adios")
except Exception as ex:
    print(ex)
except ValueError:
    print("Algo ha ido mal")
except ZeroDivisionError:
    print("Algo ha ido mal")
else:
    print("No ha habido ninguna excepción")
finally:
    print("Siempre se va ha ejecutar")
