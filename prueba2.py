class Persona():

    #constructor: define lo que puede haber y lo que no, dentro de la clase
    def __init__(self,nombre,apellidos,edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    #fin constructor
    def __str__(self):
        return self.nombre+" "+self.apellidos+" tiene "+str(self.edad)+" años."

    def mayor_de_edad(self):#no hace falta pasar edad porque ya lo has tomado en el constructor
        return self.edad >=18 #no hace falta poner if porque al hacer esa comparacion 
        #ya devuelve directamente true si se cumple o false si no se cumple
            
class Alumno(Persona):
    
    def __init_(self,nombre,apellidos,edad,asignaturas):
        super().__init__
        self.asignaturas = asignaturas

def agregar(numero,bbdd=[]):

    for i in range(numero):

        nombre = str(input("introduce tu nombre: "))
        apellidos = str(input("introduce tus apellidos: "))
        edad = int(input("introduce tu edad: "))

        bbdd.append(Persona(nombre,apellidos,edad))

    return bbdd


def mostrar(bbdd):
    for persona in bbdd:

        print(persona)


numero = int(input("introduce el numero de alumnos que va a añadir: "))

bbdd = agregar(numero)

mostrar(bbdd)