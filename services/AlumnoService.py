from model import Alumno
import Utiles

class AlumnoService:

    def set_nombre_alumno(self, alumno_parameter: Alumno):
        empty = True
        while empty:
            print("Introduzca el nombre del alumno:")
            nombre = input()
            if Utiles.is_string_valid(nombre):
                alumno_parameter.set_nombre(nombre)

            if len(alumno_parameter.get_nombre()) > 0 :
                empty = False


    def set_apellido_alumno(self, alumno_parameter: Alumno):
        empty = True
        while empty:
            print("Introduzca el apellido del alumno: ")
            apellido = input()

            if Utiles.is_string_valid(apellido):
                alumno_parameter.set_apellido(apellido)

            if len(alumno_parameter.get_apellido()) > 0:
                empty = False 

    def set_edad_alumno(self, alumno_parameter: Alumno):
        while alumno_parameter.get_edad() == 0:
            try:
                print("Introduzca la edad del alumno: ")
                edad = int(input())
                alumno_parameter.set_edad(edad)
            except ValueError:
                print("El valor introducido no es un número")


    def clonar_alumno(self, alumno_parameter: Alumno):
        alumno_clonado: Alumno = Alumno()
        alumno_clonado.set_nombre(alumno_parameter.get_nombre())

        return alumno_clonado