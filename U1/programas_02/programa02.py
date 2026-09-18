variable1 = 6
print("Tipo de 6:", type(6), "Tipo de variable1:", type(variable1))

variable2 = variable1
print("Tipo de 6:", type(6), "Tipo de variable2:", type(variable2))

print("variable1 is variable2:", variable1 is variable2)
print("variable1 is not variable2:", variable1 is not variable2)

variable1 = "Hola"
print("Tipo de 'Hola':", type("Hola"), "Tipo de variable1:", type(variable1))

print("variable2 es int:", isinstance(variable2, int))
print("variable1 es str:", isinstance(variable1, str))
