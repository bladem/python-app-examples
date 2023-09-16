from model import Alumno
from Utiles import Utiles

class AlumnoService:
    def __init__(self):
        self.alumno:Alumno = None

    def set_nombre_alumno(self, alumno_parameter: Alumno):
        empty = True
        self.alumno = alumno_parameter
        while empty:
            print("Introduzca el nombre del alumno:")
            nombre = input()
            if Utiles.is_string_valid(nombre):
                self.alumno.set_nombre(nombre)

            if len(self.alumno.get_nombre()) > 0 :
                empty = False


    def set_apellido_alumno(self):
        empty = True
        while empty:
            print("Introduzca el apellido del alumno: ")
            apellido = input()

            if Utiles.is_string_valid(apellido):
                self.alumno.set_apellido(apellido)

            if len(self.alumno.get_apellido()) > 0:
                empty = False 

    def set_edad_alumno(self):
        while self.alumno.get_edad() == 0:
            try:
                print("Introduzca la edad del alumno: ")
                edad = int(input())
                self.alumno.set_edad(edad)
            except ValueError:
                print("El valor introducido no es un número")


    def clonar_alumno(self, alumno: Alumno):
        alumno_clonado = Alumno()
        alumno_clonado.set_nombre(alumno.get_nombre())

        return alumno_clonado