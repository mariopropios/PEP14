import random

def preparar_plato(tecnica, ingredientes):
    return (tecnica * ingredientes) * random.randint(1, 4)

def mostrar_chef(nombre, tecnica, energia):
    print(f"Chef: {nombre}")
    print(f"   Técnica: {tecnica}")
    print(f"   Energía: {energia}")