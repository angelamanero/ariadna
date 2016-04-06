import sys

from modelos.alumno import Alumno
from modelos.persona import Persona

def agregar(numero, bbdd=[]): 

    for i in range(numero):

        nombre = str(input("Introduce un nombre: "))
        apellidos = str(input("Introduce tus apellidos: "))
        edad = int(input("Introduce tu edad: "))
        asignatura = str(input("Introduce tu asignatura: "))

        bbdd.append(Persona(nombre, apellidos, edad, asignatura))

    return bbdd
            
def mostrar(bbdd):
    for cosa in bbdd:
        print(cosa)

def mostrar_adultos(bbdd):
    for cosa in bbdd:
        #print(persona.mayor_de_edad)
        if  cosa.mayor_de_edad: 
            print(cosa)
                
bbdd = [Alumno('Miriam','Maillo',29,'mates'),
        Alumno('Alber','Gomez',26,'mates'),
        Alumno('Sonia', 'Perez', 15,'mates'),
        Alumno('Maria', 'Alvarez', 17,'mates')
       ]

while True:
    numero = input("Introduce el numero de alumnos que va a anadir: ")
    try:
        numero = int(numero)
        if numero >= 0:
            bbdd = agregar(numero,bbdd)
            mostrar(bbdd)
            print("Los mayores de edad son: ")
            mostrar_adultos(bbdd)
            sys.exit()
        print("no puedes poner un numero negativo")
    except Exception:
        print("valor incorrecto")
