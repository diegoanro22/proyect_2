from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import Driver


class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Login")
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

        ttk.Button(self,text="Iniciar sesión", width=20,command=lambda:self.validar(self.entryUsuario.get(),self.entryContra.get())).grid(column=1,row=5, sticky=W+E, padx=10,pady=30)
        ttk.Button(self,text="Registrarse", width=20,command=lambda:Register()).grid(column=2,row=5, sticky=W+E, padx=10,pady=30)

        self.style = ttk.Style(self)
        self.style.configure('Login.TLabel', background='#ffffff', font=("HP Simplified Hans",12))
        self.style.configure('TButton', font=("Bahnschrift",14),background="#243952")


    def validar(self,username,password):
        #Ingresa a la clase driver para verificar si el usuario y contraseña están registrados.
        try:
            self.driver = Driver.driver()
            validar_entrada = self.driver.login(username,password)

            if validar_entrada:
                Login_ven()
            else:
                pass
        except Exception as e:
            messagebox.showerror("Error",str(e))



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
        self.entryEdad.get(),self.entryNacionalidad.get(),self.entryCorreo.get(),self.entryNuevoUsuario.get(),
        self.entryNuevoContra.get())).grid(column=0,row=9, columnspan=2, sticky=W+E, padx=10,pady=30)
        
        
    def callRegistrar(self,e1,e2,e3,e4,e5,e6,e7):
        try:
            self.driver.registrarDatos(e1,e2,e3,e4,e5,e6,e7)
            self.destroy()
        except Exception:
            messagebox.showerror("Error","Ingreso un dato no válido")
            self.destroy()


class Login_ven(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        #self.driver.login()
        Toplevel.__init__(self)
        self.title("Inicio")
        self.resizable(False,False)
        self.config(bg="white")
        Label(self,text="INICIO", font=("HP Simplified Hans",16),bg="#3A495B",fg="white").grid(column=0,row=0, columnspan=2, sticky=W+E,pady=10,padx=30,ipady=10)

        ttk.Button(self,text="Ingresar IMC", width=50,command=lambda:v_imc()).grid(column=0,row=1, sticky=S+W,padx=20,pady=30,ipady=30)
        ttk.Button(self,text="Dieta", width=50, command=lambda:v_dieta()).grid(column=1,row=1, sticky=S+W,padx=20,pady=30,ipady=30)
        ttk.Button(self,text="Rutina de Ejercicios", width=50, command=lambda:v_ejercicio()).grid(column=0,row=2, sticky=S+W,padx=20,pady=30,ipady=30)
        ttk.Button(self,text="Tips", width=50, command=lambda:v_tips).grid(column=1,row=2, sticky=S+W,padx=20,pady=30,ipady=30)


class v_imc(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        Toplevel.__init__(self)
        self.title("Calculadora de IMC")
        self.resizable(False,False)
        self.config(bg="white")
        
        self.fotoimc = PhotoImage(file="IMC.png")
        Label(self,image=self.fotoimc).grid(column=0,row=5, columnspan=4,sticky=W+E)
        Label(self,text="Calcular IMC", font=("HP Simplified Hans",16),bg="#3A495B",fg="white").grid(column=0,row=0, columnspan=3, sticky=W+E,pady=10,padx=30,ipady=10)
        ttk.Label(self,text="Ingrese su altura(m)", style="Login.TLabel").grid(column=0,row=1, sticky=S+W,padx=30)
        self.entryAltura = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryAltura.grid(column=0,row=2, sticky=W+E,padx=30, ipady=5,pady=10)
        ttk.Label(self,text="Ingrese su peso(Kg)", style="Login.TLabel").grid(column=1,row=1, sticky=S+W,padx=30)
        self.entryPeso = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryPeso.grid(column=1,row=2, sticky=W+E,padx=30, ipady=5,pady=10)
        ttk.Label(self,text="Ingrese su edad", style="Login.TLabel").grid(column=2,row=1, sticky=S+W,padx=35)
        self.entryEdad = ttk.Entry(self, width=25, justify="center", font=("Century Gothic",12));self.entryEdad.grid(column=2,row=2, sticky=W+E,padx=30, ipady=5,pady=10)
        self.resultadoIMC = ttk.Label(self,text="", style="Login.TLabel").grid(column=2,row=1, sticky=S+W,padx=30)

        ttk.Button(self,text="Calcular IMC", width=20,command=lambda:self.callCalcularIMC(self.entryAltura.get(),self.entryPeso.get(),self.entryEdad.get())).grid(column=0,row=3, sticky=S+W,padx=30)
    
    def callCalcularIMC(self, altura, peso, edad):
        #try:
            self.imcfinal=self.driver.calcularIMC(altura,peso,edad)
            self.resultadoIMC = ttk.Label(self,text="Su IMC es: "+str(self.imcfinal)+" %", style="Login.TLabel").grid(column=1,row=3, columnspan=2,sticky=S+W,padx=30)
        #except:
            #messagebox.showerror("Error","Ingreso un valor erroneo")


class v_dieta(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        Toplevel.__init__(self)
        self.title("Dietas")
        self.resizable(False,False)
        self.config(bg="white")
        
        
class v_ejercicio(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        Toplevel.__init__(self)
        self.title("Ejercicios")
        self.resizable(False,False)
        self.config(bg="white")
        
        
        
        
class v_tips(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        Toplevel.__init__(self)
        self.title("Tips")
        self.resizable(False,False)
        self.config(bg="white")





app().mainloop()