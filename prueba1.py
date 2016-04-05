def agregar(numero):

    lista = []

    for i in range(numero):

        nombre = str(input("introduce un nombre: "))
        idiomas = int(input("introduce el numero de idiomas: "))

        lista.append({'nombre':nombre,'idiomas':idiomas})

    return lista


def mostrar(lista):
    for persona in lista:

            print(persona['nombre']," sabe ",persona['idiomas']," idiomas.")


numero = int(input ("introduce el numero de alumnos que va a añadir: "))

lista = agregar(numero)

mostrar(lista)