import Usuario
import IMC
import Dieta
import Archivo
import pandas as pd
import csv
import os
from random import randint

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

    def guardarArchivoDieta(self,dieta):
        if os.path.exists("Dieta.csv"):
            pass
        else:
            self.archivo.crearDieta()
        
        self.archivo.agregarDieta(dieta.__dict__)

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


    def registrarDatosIMC(self,e1,e2,e3):
        altura = str(e1)
        peso = str(e2)
        edad = int(e3)
        #Imc = str(e4)
        
        newIMC = IMC.IMC(altura,peso,edad)
        self.guardarArchivoIMC(newIMC)
        return True
    

    def calcularIMC(self, altura, peso, edad):
        altura=float(altura)
        peso=float(peso)
        edad=int(edad)
        imc=round((peso/(altura**2)),2)
        self.registrarDatosIMC(altura, peso, edad)
        return imc

    def tips_ver(self):
        can = self.archivo.leerArchivotips()
        rango = len(can)
        
        tip1= can.loc[randint(0,rango-1)].astype(str).tolist()
        
        

        return tip1[0]
    
    def obtenerTipoDieta(self):
        archivo = self.archivo.leerArchivoDieta()
        tiposDieta=set(archivo['Tipo'])
        return tiposDieta
    
    def datosDieta(self, e1, e2, e3, e4):
        if e1=="" or e2=="" or e3=="" or e4=="":
            raise Exception("Dejo algun campo en blanco")
        else:
            tipo = str(e1)
            desayuno = str(e2)
            almuerzo = str(e3)
            cena = str(e4)

            newDieta = Dieta.Dieta(tipo,desayuno,almuerzo,cena)
            self.guardarArchivoDieta(newDieta)

    def mostrarDieta(self, tipo):
        archivo=self.archivo.leerArchivoDieta()
        resultadoTipo=archivo[archivo['Tipo'].str.contains(tipo, case=False)]    
        return resultadoTipo