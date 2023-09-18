from model.Alumno import Alumno
import services.AlumnoService as alumno_service
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

alumno: Alumno = Alumno()

alumno_service.set_nombre_alumno(alumno)

alumno_service.set_apellido_alumno(alumno)
   
alumno_service.set_edad_alumno(alumno)

alumno.set_fecha_nacimiento(datetime.datetime.now())

alumno_clonado = alumno_service.clonar_alumno(alumno)

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
print("Alumno clonado: ",alumno_clonado.get_nombre(), alumno_clonado.get_apellido(), alumno_clonado.get_edad(), alumno_clonado.get_fecha_nacimiento())

print(alumno)
print(alumno_clonado)