import Usuario
import Archivo
import pandas as pd
import csv
import os

class driver():
    def __init__(self):
        self.archivo = Archivo.Archivo()

    def registrarDatos(self,e1,e2,e3,e4,e5,e6,e7):
        nombre = str(e1)
        apellido = str(e2)
        edad = int(e3)
        nacionalidad = str(e4)
        correo = str(e5)
        usuario = str(e6)
        contraseña = str(e7)
        
        newUsuario = Usuario.Usuario(nombre,apellido,edad,nacionalidad,correo,usuario,contraseña)
        self.guardarArchivo(newUsuario)


    def guardarArchivo(self,usuario):
        if os.path.exists("Usuarios.csv"):
            pass
        else:
            self.archivo.crearArchivo()
        
        self.archivo.agregarUsuario(usuario.__dict__)


    def login(self, username, password):
        archivo = self.archivo.leerArchivo()
        
        if username =="" or password == "":
            raise Exception ("No llenó el formulario")

        filtro_user = archivo.loc[archivo["usuario"] == username]
        if filtro_user.empty:
            raise Exception("Usuario no encontrado")
        
        filtro_pass = archivo.loc[(archivo["usuario"] == username) & (archivo["_Usuario__contraseña"] == password)]
        if filtro_pass.empty:
            raise Exception("Contraseña incorrecta")

        return True
    

    def calcularIMC(self, altura, peso, edad):
        altura=float(altura)
        peso=float(peso)
        edad=int(edad)
        imc=round((peso/(altura**2)),2)
        return imc