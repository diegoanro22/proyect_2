import Usuario
import IMC
import Dieta
import Archivo
import pandas as pd
import os

from random import randint

import Ejercicio


class driver():
    def __init__(self):
        """
         Metodo que inicia el objeto Archivo de la clase establecida en el
        """
        self.archivo = Archivo.Archivo()

    def registrarDatos(self,e1,e2,e3,e4,e5,e6,e7):
        """
         Registra los datos del usuario en la base de datos. Si se puede guardar el archivo de usuario no haya registrarlos o guardar el archivo aleatorio.
         
         @param e1 - Numero de elementos a mostrar.
         @param e2 - Numero de elementos a mostrar.
         @param e3 - Escolhía que indica el nuevo elemento.
         @param e4 - Escolhía que indica el nuevo elemento.
         @param e5 - Numero de elementos a mostrar.
         @param e6 - El numero de elementos a mostrar.
         @param e7 - El numero de elementos a mostrar
        """
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
        """
         Guarda el archivo de acuerdo a la entidad. Si existe en caso de no se haya el archivo crea y agregamos el usuario
         
         @param usuario - Objeto que contiene los datos de la entid
        """
        # Metodo para crear archivo de archivo de archivo.
        if os.path.exists("Usuarios.csv"):
            pass
        else:
            self.archivo.crearArchivo()
        self.archivo.agregarUsuario(usuario.__dict__)

    def guardarArchivoIMC(self,imc):
        """
         Guarda el archivo de IMC si existe en la base de datos. Si no existe crea el objeto imc aplicar al usuario
         
         @param imc - Objeto que contiene los
        """
        # Metodo para crearIMC. csv del archivo. csv
        if os.path.exists("IMC.csv"):
            pass
        else:
            self.archivo.crearIMC()
        self.archivo.agregarIMC(imc.__dict__)

    def guardarArchivoDieta(self,dieta):
        """
         Guarda el archivo de dieta a la ventana. Si existe la ruta de un fichero dieta se realiza con lo contrario devuelve el objeto
         
         @param dieta - Objeto que contiene los
        """
        # Devuelve el dieta. csv del archivo dieta. csv
        if os.path.exists("Dieta.csv"):
            pass
        else:
            self.archivo.crearDieta()
        
        self.archivo.agregarDieta(dieta.__dict__)

    def login(self, username, password):
        """
         Metodo que permite logins a usuario en la base de datos. This is a convierte el formulario de usuario y el password de usuario
         
         @param username - Nombre del usuario que se desea logging in
         @param password - Password de usuario que se desea logging in
         
         @return True si hay correctamente False en caso contrario o exception que se debe c
        """
        archivo = self.archivo.leerArchivo()
        
        # El formulario el formulario del formulario
        if username =="" or password == "":
            raise Exception ("No llenó el formulario")

        filtro_user = archivo.loc[archivo["usuario"] == username]
        # Metodo para filtro_user. empty encontrado en el user
        if filtro_user.empty:
            raise Exception("Usuario no encontrado")
        
        filtro_pass = archivo.loc[(archivo["usuario"] == username) & (archivo["_Usuario__contraseña"] == password)]
        # Contraseña incorrecta a incorrecta.
        if filtro_pass.empty:
            raise Exception("Contraseña incorrecta")

        return True


    def registrarDatosIMC(self,e1,e2,e3):
        """
         Registra los datos de la IMC en el sistema. Devuelve True
         
         @param e1 - Altura a registrar. Se encuentra como parametro.
         @param e2 - Peso a registrar. Se encuentra como parametro.
         @param e3 - Ejemplo de modificacion del dato.
         
         @return Retorna True si se hay success
        """
        altura = str(e1)
        peso = str(e2)
        edad = int(e3)
        #Imc = str(e4)
        
        newIMC = IMC.IMC(altura,peso,edad)
        self.guardarArchivoIMC(newIMC)
        return True
    

    def calcularIMC(self, altura, peso, edad):
        """
         Calcula el imc de cada altura y peso. Esta funcion es llamada a la informacion de los datos en el servidor.
         
         @param altura - Altura a realizar ( mensaje ).
         @param peso - Peso a realizar ( fecha ).
         @param edad - Edda de la base de datos.
         
         @return Numero de imc de cada altura y peso ( float ). Si es igual devuelve un float
        """
        altura=float(altura)
        peso=float(peso)
        edad=int(edad)
        imc=round((peso/(altura**2)),2)
        self.registrarDatosIMC(altura, peso, edad)
        return imc


    def tips_ver(self):
        """
         Devuelve un mensaje de tipos aleatoriamente. Retorna una cantidad de tipos
         
         
         @return tipos aleatoriamente para el
        """
        can = self.archivo.leerArchivotips()
        rango = len(can)
        
        tip1= can.loc[randint(0,rango-1)].astype(str).tolist()
        
        

        return tip1[0]
    
    def obtenerTipoDieta(self):
        """
         Obtiene una lista de tipos de dieta del sistema. Devuelve una lista desde la clase TiposDieta
         
         
         @return lista de tipos de di
        """
        archivo = self.archivo.leerArchivoDieta()
        tiposDieta=set(archivo['Tipo'])
        return tiposDieta
    
    def datosDieta(self, e1, e2, e3, e4):
        """
         Metodo que permite crear un archivo de dieta con los datos recibidos
         
         @param e1 - El tipo de la direccion a mostrar. Ejemplo : tipo = " Tipo " desayuno = " Dejemplo "
         @param e2 - El desayuno de la direccion a mostrar. Ejemplo : desayuno = " De
         @param e3
         @param e4
        """
        # Guarda un Dieta para guardar de la guardar de la archivo de la guardar de la guardar de la archivo dieta.
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
        """
         Muestra un objeto de tipo dieta que contiene la informacion dentro
         
         @param tipo - Nombre del tipo a mostrar
         
         @return Retorna el objeto de tipo dieta que contiene la informacion dentro
        """
        archivo=self.archivo.leerArchivoDieta()
        resultadoTipo=archivo[archivo['Tipo'].str.contains(tipo, case=False)]    
        return resultadoTipo

    def obtenerGrupo(self):
        """
         Obtiene los grupos musculados del archivo. Devuelve una lista de nombres de grupos musculados
         
         
         @return lista de nombres de grup
        """
        archivo = self.archivo.leerArchivoRutina()
        grupos_musculares = set(archivo['Grupo_Muscular'])
        return grupos_musculares

    def obtenerEjercicio(self,grupo):
        """
         Devuelve una lista contenida de los ejercicios que coinciden con el grupo
         
         @param grupo - El grupo que se desea obtener
         
         @return Los ejercicios que coinciden con el grupo ( diccionario
        """
        archivo = self.archivo.leerArchivoRutina()
        ejercicios_grupo = archivo[archivo['Grupo_Muscular'] == grupo]
        return ejercicios_grupo
    
    def registrarEjercicio(self,e1,e2,e3,e4):
        """
         Registra un ejercicio en la base de datos. Cada estructura de este clase Ejercicio y guarda el ultimo objeto
         
         @param e1 - La ruta dentro del grupo de la ejercicio
         @param e2 - La ruta dentro del nombre de la ejercicio
         @param e3 - La ruta direccion de la ejercicio
         @param e4 - La ruta direccion de la ejercic
        """
        grupo = str(e1)
        nombre = str(e2)
        sets = int(e3)
        reps = int(e4)
        newEjercicio = Ejercicio.Ejercicio(grupo,nombre,sets,reps)
        self.guardarEjercicio(newEjercicio)
        
    def guardarEjercicio(self,ejercicio):
        """
         Guarda el ejercicio en la base de datos. Si existe la rutina de entrada no agregar el ejercicio
         
         @param ejercicio - Objeto que contiene los datos de la ej
        """
        # Metodo para crear Rutina. csv del archivo
        if os.path.exists("Rutina.csv"):
            pass
        else:
            self.archivo.crearRutina()
        self.archivo.agregarEjercicio(ejercicio.__dict__)

