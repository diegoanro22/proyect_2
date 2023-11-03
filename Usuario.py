class Usuario():
    def __init__(self,nombre,apellido,edad,nacionalidad,correo,usuario,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.correo = correo
        self.usuario = usuario
        self.contraseña = contraseña
    
    def getNombre(self):
        return self.nombre
    
    