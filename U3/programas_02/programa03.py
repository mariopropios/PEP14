"""
Escribe un programa que use los módulos platform y os para,
     Mostrar el procesador donde se ejecuta el programa.
     Mostrar el sistema operativo y versión donde se ejecuta el programa.
     Mostrar el nombre el host donde se ejecuta el programa.
     Mostrar el directorio actual.
"""
import platform
import os

print("Procesador:", platform.processor())
print("Sistema operativo:", platform.system())
print("Version:", platform.version())
print("Host:", platform.node())
print("Directorio actual:", os.getcwd())