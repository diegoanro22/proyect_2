import Usuario
import IMC
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

    def guardarArchivoIMC(self,imc):
        if os.path.exists("IMC.csv"):
            pass
        else:
            self.archivo.crearIMC()
        
        self.archivo.agregarIMC(imc.__dict__)


    def login(self, username, password):
        archivo = self.archivo.leerArchivo()
        
        if username =="" or password == "":
            raise Exception ("No llenó el formulario")

        filtro_user = archivo.loc[archivo["usuario"] == username]
        if filtro_user.empty:
            raise Exception("Usuario no encontrado")
        
<<<<<<< HEAD
        filtro_pass = archivo.loc[(archivo["usuario"] == username) & (archivo["_Usuario__contraseña"] == password)]
        if filtro_pass.empty:
            raise Exception("Contraseña incorrecta")
=======
        filtro = archivo.loc[archivo["usuario"] == username]
        filtropass = archivo.loc[archivo["_Usuario__contraseña"] == password]
        if filtro.empty == True and filtropass.empty == True:
            return False
        else:
            return True
        print(filtro)

        # if username =="" or password == "":
        #    raise Exception ("asd")

    def registrarDatosIMC(self,e1,e2,e3):
        altura = str(e1)
        peso = str(e2)
        edad = int(e3)
        #Imc = str(e4)
        
        newIMC = IMC.IMC(altura,peso,edad)
        self.guardarArchivoIMC(newIMC)

>>>>>>> e35638bc3353d222e6bc86d4d09ff7dbf009e9db

        return True
    

    def calcularIMC(self, altura, peso, edad):
        altura=float(altura)
        peso=float(peso)
        edad=int(edad)
        imc=round((peso/(altura**2)),2)
        self.registrarDatosIMC(altura, peso, edad)
        return imc


    

