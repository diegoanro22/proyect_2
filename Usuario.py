
from typing import Any


class Usuario():
    def __init__(self,nombre,apellido,edad,nacionalidad,correo,usuario,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.correo = correo
        self.usuario = usuario
        self.__contraseña = contraseña

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getApeliido(self):
        return self.apellido
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def getEdad(self):
        return self.edad
    
    def setEdad(self, edad):
        self.edad = edad

    def getNacionalidad(self):
        return self.nacionalidad

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def getCorreo(self):
        return self.correo
    
    def setCorreo(self, correo):
        self.correo = correo

    def getUsuario(self):
        return self.usuario
    
    def setUsuario(self, usuario):
        self.usuario = usuario

    def getContraseña(self):
        return self.__contraseña
    

    def toString(self):
        return f"{self.getNombre()},{self.getApeliido()},{self.getEdad()},{self.getNacionalidad()},{self.getCorreo()},{self.getUsuario()},{self.getContraseña()}"
