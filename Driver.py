import Usuario
import IMC
import Archivo
import pandas as pd
import os
import Ejercicio

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

    def obtenerGrupo(self):
        archivo = self.archivo.leerArchivoRutina()
        grupos_musculares = set(archivo['Grupo_Muscular'])
        return grupos_musculares

    def obtenerEjercicio(self,grupo):
        archivo = self.archivo.leerArchivoRutina()
        ejercicios_grupo = archivo[archivo['Grupo_Muscular'] == grupo]
        return ejercicios_grupo
    
    def registrarEjercicio(self,e1,e2,e3,e4):
        grupo = str(e1)
        nombre = str(e2)
        sets = int(e3)
        reps = int(e4)
        newEjercicio = Ejercicio.Ejercicio(grupo,nombre,sets,reps)
        self.guardarEjercicio(newEjercicio)
        
    def guardarEjercicio(self,ejercicio):
        if os.path.exists("Rutina.csv"):
            pass
        else:
            self.archivo.crearRutina()
        self.archivo.agregarEjercicio(ejercicio.__dict__)