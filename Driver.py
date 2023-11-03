import Usuario


class driver():
    def __init__(self):
        pass
    
    def registrarDatos(self):
        nombre = str(self.entryEdad.get())
        apellido = str(self.entryApellido.get())
        edad = int(self.entryEdad.get())
        nacionalidad = str(self.entryNacionalidad.get())
        correo = str(self.entryCorreo.get())
        usuario = str(self.entryNuevoUsuario.get())
        contraseña = str(self.entryNuevoContra.get())
        
        newUsuario = Usuario.Usuario(nombre,apellido,edad,nacionalidad,correo,usuario,contraseña)
        print(newUsuario)
        print(newUsuario.getNombre())

    def calcularIMC():
        pass