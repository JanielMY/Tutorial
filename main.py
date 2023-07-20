nombre, edad, sexo, zurdo = "Janiel Marquez", 17, "masulino", False

# cammelCase
# snake_case

# COMENTARIO SOLITO

"""
COMENTARIO DE MULTIPLES LINEAS
"""

print(f'Mi nombre es {nombre} tengo {edad} años')
if zurdo:
    print("soy zurdo")

elif not zurdo:
    print("hola")


def miFuncion(x):
    x=5
    print(x)


x = 10 # Variable global
miFuncion(x)