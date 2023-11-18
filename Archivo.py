import pandas as pd
import os

class Archivo():
    def __init__(self) :
        """
         Initialize the object. This is called by __init__ and should not be called directly by user code
        """
        pass
    
    def crearArchivo(self):
        """
         Crea un archivo a partir de usuarios. csv y no han sido
        """
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
        """
         Crea el IMC a partir desde la tabla IMC. csv y los cambios
        """
        df = pd.DataFrame()
        df['Altura'] = None
        df['Peso'] = None
        df['Edad'] = None      
        df.to_csv("IMC.csv",index=False, mode="a")

    def crearDieta(self):
        """
         Crea el Dieta a partir de la tabla Dieta. csv y los valores
        """
        df = pd.DataFrame()
        df['Tipo'] = None
        df['desayuno'] = None
        df['almuerzo'] = None
        df['cena'] = None
        df.to_csv("Dieta.csv",index=False, mode="a")

    def crearTips(self):
        """
         Crea el fichero de tipes a partir desde la tabla Tips.
        """
        df = pd.DataFrame()
        df['tip'] = None
        df.to_csv("Tips.csv",index=False, mode="a")

    def crearRutina(self):
        """
         Crea el rutina de acuerdo a la tabla Rutina. csv con los nombres de gro
        """
        df = pd.DataFrame()
        df['Grupo_Muscular'] = None
        df['nombre'] = None
        df['sets'] = None
        df['repeticiones'] = None
        df.to_csv("Rutina.csv",index=False, mode="a")

    def leerArchivo(self):
        """
         Lee un archivo de usuarios. Carga una tabla de usuarios
         
         
         @return Diccion de archivos a leer
        """
        df = pd.read_csv("Usuarios.csv")
        return df


    def leerArchivoIMC(self):
        """
         Devuelve una tabla de imc en formato IMC. csv. Se retorna un diccionario con los datos del archivo IMC.
         
         
         @return Dadastro de datos del archivo
        """
        df = pd.read_csv("IMC.csv")
        return df
    
    def leerArchivotips(self):
        """
         Leer Archivotips. This is a dataframe that contains information about the Tips that are part of the archive.
         
         
         @return A dataframe with the following columns : Tips ( str ) : Name of the file that contains the
        """
        df = pd.read_csv("Tips.csv")
        
        return df
    
    def leerArchivoDieta(self):
        """
         Lee un archivo dieta enviado como parametro. Si se encuentra la tabla de dieta dieta aleatorio
         
         
         @return Devuelve una tabla de dieta
        """
        df = pd.read_csv("Dieta.csv")

        return df

    def leerArchivoRutina(self):
        """
         Lee el archivo de rutina y devuelve una tabla de todos los registros
         
         
         @return Diccion de registros en formato pandas. Dataframe ( dataframe ) con los datos del arch
        """
        df = pd.read_csv("Rutina.csv")
        return df
        


    def agregarUsuario(self,usuario):
        """
         Agrega un usuario en la tabla Usuarios. csv y leer el archivo
         
         @param usuario - La cantidad de usuar
        """
        df = self.leerArchivo()
        ndf = pd.DataFrame(usuario,index=[0])
        df = pd.concat([ndf],ignore_index=False)
        df.to_csv("Usuarios.csv",index=False, mode="a", header=not os.path.isfile("Usuarios.csv"))

    def agregarIMC(self,imc):
        """
         Agrega el IMC a la tabla imc. csv y le ejecuta en el archivo
         
         @param imc - Dataframe contenidos de la tab
        """
        df = self.leerArchivoIMC()
        ndf = pd.DataFrame(imc,index=[0])
        df = pd.concat([ndf],ignore_index=False)
        df.to_csv("IMC.csv",index=False, mode="a", header=not os.path.isfile("IMC.csv"))


        
    def agregarDieta(self,dieta):
        """
         Agrega un archivo dieta a la tabla Dieta. csv y le ejecuta la cantidad de registros
         
         @param dieta - La cadena de la forma di
        """
        df = self.leerArchivo()
        ndf = pd.DataFrame(dieta,index=[0])
        df = pd.concat([ndf],ignore_index=False)
        df.to_csv("Dieta.csv", index=False, mode="a", header=not os.path.isfile("Dieta.csv"))

    def agregarEjercicio(self,ejercicio):
        """
         Agrega el archivo de la ejercicio y leer en el Rutina. csv
         
         @param ejercicio - estrutura del fichero a agreg
        """
        df = self.leerArchivo()
        ndf = pd.DataFrame(ejercicio,index=[0])
        df = pd.concat([ndf],ignore_index=False)
        df.to_csv("Rutina.csv",index=False, mode="a", header=not os.path.isfile("Rutina.csv"))
        

