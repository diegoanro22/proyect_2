import pandas as pd
import os

class Archivo():
    def __init__(self) :
        pass
    
    def crearArchivo(self):
        df = pd.DataFrame()
        df['ID'] = None
        df['Nombre'] = None
        df['Apellido'] = None
        df['Edad']= None
        df['Nacionalidad'] = None
        df['Correo Electronico'] = None
        df['Usuario'] = None
        df['Contraseña'] = None        
        df.to_csv("Usuarios.csv",index=False, mode="r")

    def crearIMC(self):
        df = pd.DataFrame()
        df['Altura'] = None
        df['Peso'] = None
        df['Edad'] = None      
        df.to_csv("IMC.csv",index=False, mode="r")

    def crearDieta(self):
        df = pd.DataFrame()
        df['Tipo'] = None
        df['desayuno'] = None
        df['almuerzo'] = None
        df['cena'] = None
        df.to_csv("Dieta.csv",index=False, mode="r")

    def crearTips(self):
        df = pd.DataFrame()
        df['tip'] = None
        df.to_csv("Tips.csv",index=False, mode="r")

    def crearRutina(self):
        df = pd.DataFrame()
        df['Grupo_Muscular'] = None
        df['nombre'] = None
        df['sets'] = None
        df['repeticiones'] = None
        df.to_csv("Rutina.csv",index=False, mode="r")

    def leerArchivo(self):
        df = pd.read_csv("Usuarios.csv")
        
        return df


    def leerArchivoIMC(self):
        df = pd.read_csv("IMC.csv")
        
        return df



    def agregarUsuario(self,usuario):
        df = self.leerArchivo()
        ndf = pd.DataFrame(usuario,index=[0])
        df = pd.concat([ndf],ignore_index=False)
        df.to_csv("Usuarios.csv",index=False, mode="a", header=not os.path.isfile("Usuarios.csv"))

    def agregarIMC(self,imc):
        df = self.leerArchivoIMC()
        ndf = pd.DataFrame(imc,index=[0])
        df = pd.concat([ndf],ignore_index=False)
        df.to_csv("IMC.csv",index=False, mode="a", header=not os.path.isfile("IMC.csv"))

        
        
