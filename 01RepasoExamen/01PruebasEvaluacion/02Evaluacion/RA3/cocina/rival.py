import random

def generar_rival():
    nombres = ["Gordon", "Arguiñano", "Massimo", "SaltBae", "Dacosta"]
    nombre = random.choice(nombres)
    tecnica = random.randint(1, 10)
    energia = random.randint(1, 5)
    return nombre, tecnica, energia

def preparar_plato_rival(tecnica, ingredientes):
    return (tecnica * ingredientes) * random.randint(1, 4)

def mostrar_rival(nombre, tecnica, energia):
    print(f"Rival: {nombre}")
    print(f"   Técnica: {tecnica}")
    print(f"   Energía: {energia}")