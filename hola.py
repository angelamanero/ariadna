
import math
t = "%(nombre)s sabe %(idiomas)i idiomas"

v = [{'nombre':'angela', 'idiomas':5}, {'nombre':'marina', 'idiomas':3}]

def funcion1(nombre, idiomas):
    return nombre, " tiene ", idiomas, " idiomas."

for persona in v:
    print funcion1(persona['nombre'], persona['idiomas'])