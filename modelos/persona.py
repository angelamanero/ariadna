class Persona():
    
    #constructor: define lo que puede haber y lo que no, dentro de la clase
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def __str__(self):
        return self.nombre+" "+self.apellidos+", "+str(self.edad)

    @property    #para poder llamar a una función sin los corchetes   
    def mayor_de_edad(self):#no hace falta pasar edad porque ya lo has tomado en el constructor
        return self.edad >=18 #no hace falta poner if porque al hacer esa comparacion 
        #ya devuelve directamente true si se cumple o false si no se cumple
        return self.edad >= 18