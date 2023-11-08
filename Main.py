from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import Usuario
import Driver


class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Menú Principal")
        self.config(bg="white")
        self.resizable(False,False)        
        self.login()
        


    def login(self):
        self.foto = PhotoImage(file="Logo.png")
        Label(self,image=self.foto).grid(column=0,row=0,rowspan=6)
        Label(self,text="Login", font=("HP Simplified Hans",16),bg="#3A495B",fg="white").grid(column=1,row=0, columnspan=2, sticky=W+E,pady=10,padx=50,ipady=10)
        
        ttk.Label(self,text="Usuario", style="Login.TLabel").grid(column=1,row=1, sticky=S+W,padx=50)
        self.entryUsuario = ttk.Entry(self, width=50, justify="center", font=("Century Gothic",12));self.entryUsuario.grid(column=1,row=2, columnspan=2, sticky=W+E,padx=50, ipady=5)
        ttk.Label(self,text="Contraseña",style="Login.TLabel").grid(column=1,row=3, sticky=S+W,padx=50)
        self.entryContra = ttk.Entry(self, show="*",width=50, justify="center",font=("Century Gothic",12));self.entryContra.grid(column=1,row=4, columnspan=2, sticky=W+E,padx=50,ipady=5)

        ttk.Button(self,text="Iniciar sesión", width=20).grid(column=1,row=5, sticky=W+E, padx=10,pady=30)
        ttk.Button(self,text="Registrarse", width=20,command=lambda:Register()).grid(column=2,row=5, sticky=W+E, padx=10,pady=30)

        self.style = ttk.Style(self)
        self.style.configure('Login.TLabel', background='#ffffff', font=("HP Simplified Hans",12))
        self.style.configure('TButton', font=("Bahnschrift",14),background="#243952")


class Register(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        Toplevel.__init__(self)
        self.title("Registrarse")
        self.resizable(False,False)   
        self.config(bg="white")
        Label(self,text="Registro", font=("HP Simplified Hans",16),bg="#3A495B",fg="white").grid(column=0,row=0, columnspan=2, sticky=W+E,pady=10,padx=30,ipady=10)
        
        ttk.Label(self,text="Nombres", style="Login.TLabel").grid(column=0,row=1, sticky=S+W,padx=30)
        ttk.Label(self,text="Apellidos", style="Login.TLabel").grid(column=1,row=1, sticky=S+W,padx=30)
        self.entryName = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryName.grid(column=0,row=2, sticky=W+E,padx=30, ipady=5,pady=10)
        self.entryApellido = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryApellido.grid(column=1,row=2, sticky=W+E,padx=30, ipady=5,pady=10)

        ttk.Label(self,text="Edad", style="Login.TLabel").grid(column=0,row=3, sticky=S+W,padx=30)
        ttk.Label(self,text="Nacionalidad", style="Login.TLabel").grid(column=1,row=3, sticky=S+W,padx=30)
        self.entryEdad = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryEdad.grid(column=0,row=4, sticky=W+E,padx=30, ipady=5,pady=10)
        self.entryNacionalidad = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryNacionalidad.grid(column=1,row=4, sticky=W+E,padx=30, ipady=5,pady=10)

        ttk.Label(self,text="Correo electronico", style="Login.TLabel").grid(column=0,row=5, sticky=S+W,padx=30)
        self.entryCorreo = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryCorreo.grid(column=0,row=6, columnspan=2, sticky=W+E,padx=30, ipady=5,pady=10)
        
        ttk.Label(self,text="Usuario", style="Login.TLabel").grid(column=0,row=7, sticky=S+W,padx=30)
        ttk.Label(self,text="Contraseña", style="Login.TLabel").grid(column=1,row=7, sticky=S+W,padx=30)
        self.entryNuevoUsuario = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryNuevoUsuario.grid(column=0,row=8, sticky=W+E,padx=30, ipady=5,pady=10)
        self.entryNuevoContra = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryNuevoContra.grid(column=1,row=8, sticky=W+E,padx=30, ipady=5,pady=10)
        
        ttk.Button(self,text="Registrar", width=20, command=lambda:self.callRegistrar(self.entryName.get(),self.entryApellido.get(),
        self.entryEdad.get(),self.entryNacionalidad.get(),self.entryCorreo.get(),self.entryNuevoUsuario.get(),self.entryNuevoContra.get())).grid(column=0,row=9, columnspan=2, sticky=W+E, padx=10,pady=30)
        
        
    def callRegistrar(self,e1,e2,e3,e4,e5,e6,e7):
        try:
            self.driver.registrarDatos(e1,e2,e3,e4,e5,e6,e7)
        except Exception:
            messagebox.showerror("Error","Ingreso un dato no válido")
            self.destroy()




app().mainloop()