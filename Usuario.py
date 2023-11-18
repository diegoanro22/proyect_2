
from typing import Any


class Usuario():
    def __init__(self,nombre,apellido,edad,nacionalidad,correo,usuario,contraseña):
        """
         Inicializa el objeto de la clase con los atributos correspondiente a la entidad
         
         @param nombre - Nombre del registro a cargar
         @param apellido - Apellido del registro a cargar
         @param edad - Educion de un nuevo registro en la pantalla
         @param nacionalidad - Nombre del registro a cargar
         @param correo - Correo que pertenece el registro
         @param usuario - Usuario que pertenece el registro a c
         @param contraseña
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.correo = correo
        self.usuario = usuario
        self.__contraseña = contraseña

    def getNombre(self):
        """
         Devuelve el nombre de la ventana. Creada los parametros establecidos en el archivo de manera que haya la ventana.
         
         
         @return Nombre de la ventana ( int ) or None if no existe ( bool ). False si no existe
        """
        return self.nombre
    
    def setNombre(self, nombre):
        """
         Set el nombre de la pantalla. Luego de esta clase se encuentra en el archivo CADA_NOMBRE
         
         @param nombre - La cadena de la pantall
        """
        self.nombre = nombre

    def getApeliido(self):
        """
         Devuelve el apelido del usuario. Debe ser una cadena de caracteres que contiene en el objeto CADA_APELIDO
         
         
         @return Devuelve el apelido del usu
        """
        return self.apellido
    
    def setApellido(self, apellido):
        """
         Sets apellido of the person. It is used to check if the person is indeed a part of the group
         
         @param apellido - A string that is the ap
        """
        self.apellido = apellido

    def getEdad(self):
        """
         Returns edad information. This is a read - only property. It can be used to read the data that is stored in the EDIC file or to write a new EDIC file.
         
         
         @return a L { Deferred } which fires with a list of C { str } s that represent the EDAD
        """
        return self.edad
    
    def setEdad(self, edad):
        """
         Set the edad to use for this channel. This is a bit tricky because we don't have a way to know what is going on on the EDAD and it's easier to do it in one place.
         
         @param edad - The edad to use for this channel
        """
        self.edad = edad

    def getNacionalidad(self):
        """
         Devuelve el nacionalidad del objeto Cadena de la clase Nacionalidad
         
         
         @return Devuelve el nacionalidad del objeto Cadena de la clase Nacion
        """
        return self.nacionalidad

    def setNacionalidad(self, nacionalidad):
        """
         Set the nacionalidad of the pet. It is used to check if the pet is valid
         
         @param nacionalidad - the nacionalidad of the
        """
        self.nacionalidad = nacionalidad

    def getCorreo(self):
        """
         Retorna el correo a partir de la ventana. Devuelve el objeto que representa la correo
         
         
         @return el numero de la
        """
        return self.correo
    
    def setCorreo(self, correo):
        """
         Set the correo to use for this event. This is a wrapper around L { setCorreo }
         
         @param correo - The correo to use
        """
        self.correo = correo

    def getUsuario(self):
        """
         Devuelve el usuario del objeto Cadena de la clase que contiene en el sistema
         
         
         @return Cadena de la cl
        """
        return self.usuario
    
    def setUsuario(self, usuario):
        """
         Sets the usuario that this instance is associated with. This is a convenience method for subclasses to override in order to provide a custom implementation.
         
         @param usuario - The usuario that this instance is associated with
        """
        self.usuario = usuario

    def getContraseña(self):
        """
         Return the contraseña of the object. Note that this is a copy of the data in the object not a copy of the object itself.
         
         
         @return contraseña of the object as a L { Deferred } which fires with a L { str }
        """
        return self.__contraseña
    

    def toString(self):
        """
         Devuelve una cadena de texto con los atributos del objeto Codigo.
         
         
         @return Codigo de texto con los atributos del objeto Codigo. >>> from pymel. core import Financial >>> Financial. from_string ( " Franco " )
        """
        return f"{self.getNombre()},{self.getApeliido()},{self.getEdad()},{self.getNacionalidad()},{self.getCorreo()},{self.getUsuario()},{self.getContraseña()}"
