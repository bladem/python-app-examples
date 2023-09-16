import datetime

class Alumno:
    __nombre: str
    __apellido: str
    __edad: int = 0
    __fecha_nacimiento: datetime

    def __init__(self):
        print("Inicio constructor vacio")
        
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_edad(self):
        return self.__edad
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento


    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self, apellido):
        self.__apellido = apellido
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento   