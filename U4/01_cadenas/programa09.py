"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Muestra el código Unicode de un emoji (ord(), hex()).
     Crea un carácter a partir de un código numérico (chr()).
     Imprime los caracteres ASCII del 48 al 57 (dígitos) en una línea.

"""

emoji = "😀"
codigo = ord(emoji)

print(f"Emoji: {emoji}")

print(f"Código decimal: {codigo}")

print(f"Código hexadecimal: {hex(codigo)}")

print("chr(65):", chr(65))

print("chr(241):", chr(241))

for codigo_ascii in range(48, 58):
    print(chr(codigo_ascii), end=" ")
print()