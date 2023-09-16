from Utiles import Utiles
from model.Alumno import Alumno
from model.Persona import Persona
import datetime

correcto = False



while correcto == False:
    try:
        print("Elija el tamaño de la lista: (Debe ser mayor a 0)")
        sizeLista = int(input())      

        if sizeLista > 0:
            correcto = True
        else:
            print("El valor introducido es 0 y no está permitido")
    except ValueError:
        print("El dato introducido no es un numero")

empty = True

alumno = Alumno()
persona = Persona()

while empty:
    print("Introduzca el nombre del alumno:")
    nombre = input()
    if Utiles.is_string_valid(nombre):
        alumno.set_nombre(nombre)
        persona.nombre = nombre
    if len(alumno.get_nombre()) > 0 :
        empty = False


empty = True

while empty:
    print("Introduzca el apellido del alumno: ")
    apellido = input()

    if Utiles.is_string_valid(apellido):
        alumno.set_apellido(apellido)
        persona.apellido = apellido

    if len(alumno.get_apellido()) > 0:
        empty = False    

print(type(alumno.get_edad()))

while alumno.get_edad() == 0:
    try:
        print("Introduzca la edad del alumno: ")
        edad = int(input())
        alumno.set_edad(edad)
        persona.edad = edad
    except ValueError:
        print("El valor introducido no es un número")

alumno.set_fecha_nacimiento(datetime.datetime.now())
persona.fecha_nacimiento = datetime.datetime.now();

i = 1

lista = []

while i <= sizeLista:
    print("El valor de i es: ", i)
    lista.append(i)

    if i == 5:
        print("El numero es 5")
    elif i >5 and i < 9:
        print("El numero está entre 5 y 9")
    else:
        print("El numero no es 5")

    i = i +1
    

print(lista)
print(len(lista))
print("Alumno: ",alumno.get_nombre(), alumno.get_apellido(), alumno.get_edad(), alumno.get_fecha_nacimiento())
print("Persona: ", persona.nombre, persona.apellido, persona.edad, persona.fecha_nacimiento)