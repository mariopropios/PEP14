def a_binario(n):
    return bin(n)


def a_hexadecimal(n):
    return hex(n)


def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return "El texto no es un numero entero valido"