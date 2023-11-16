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
        df.to_csv("Usuarios.csv",index=False, mode="a")

    def crearIMC(self):
        df = pd.DataFrame()
        df['Altura'] = None
        df['Peso'] = None
        df['Edad'] = None       
        df.to_csv("IMC.csv",index=False, mode="a")


    def leerArchivo(self):
        df = pd.read_csv("Usuarios.csv")
        return df


    def agregarIMC(self):
        pass


    def agregarUsuario(self,usuario):
        df = self.leerArchivo()
        ndf = pd.DataFrame(usuario,index=[0])
        df = pd.concat([ndf],ignore_index=False)
        df.to_csv("Usuarios.csv",index=False, mode="a", header=not os.path.isfile("Usuarios.csv"))
        
        
