"""
Escribe un programa en Python que realice que extraiga el nombre de usuario y la
contraseña de la siguiente cadena: "usuario:root|contraseña:123456"
"""
datos = "usuario:root|contraseña:123456"

partes = datos.split("|")

usuario = partes[0].split(":")[1]
contrasena = partes[1].split(":")[1]

print("Usuario:", usuario)
print("Contraseña:", contrasena)