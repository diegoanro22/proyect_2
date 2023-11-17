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
        ttk.Button(self,text="Tips", width=50, command=lambda:v_tips()).grid(column=1,row=2, sticky=S+W,padx=20,pady=30,ipady=30)


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
        try:
            self.imcfinal=self.driver.calcularIMC(altura,peso,edad)
            self.resultadoIMC = ttk.Label(self,text="Su IMC es: "+str(self.imcfinal)+" %", style="Login.TLabel").grid(column=1,row=3, columnspan=2,sticky=S+W,padx=30)
        except:
            messagebox.showerror("Error","Ingreso un valor erroneo")


class v_dieta(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        Toplevel.__init__(self)
        self.title("Dietas")
        self.resizable(False,False)
        self.config(bg="white")
        self.tab=ttk.Notebook(self)
        self.tab.grid(column=0,row=0)

        self.tab1=ttk.Frame(self.tab)
        self.tab2=ttk.Frame(self.tab)

        self.tab.add(self.tab1,text="Mostrar Dieta")
        self.tab.add(self.tab2,text="Ingresar Dieta")
        style=ttk.Style()
        style.configure("TNotebook.Tab", background="white", font=("Bahnschrift", 18), foreground="#3A495B")
        style.configure("TFrame", background="white", font=("Bahnschift",18), foreground="#3A495B")

        ttk.Label(self.tab1,text="Seleccione el tipo de dieta que desea ver", style="Login.TLabel").grid(column=0,row=0, sticky=S+W,padx=30)
        self.combobox=ttk.Combobox(self.tab1)
        self.combobox['values']=tuple(self.driver.obtenerTipoDieta())
        self.combobox.set('Seleccione una opción')
        self.combobox.grid(column=0,row=1, sticky=S+W, padx=30)

        ttk.Label(self.tab2,text="Ingrese el tipo de su dieta: ", style="Login.TLabel").grid(column=0,row=0, sticky=S+W,padx=30)
        self.entryTipo = ttk.Entry(self.tab2, width=25, justify="center", font=("Century Gothic",12));self.entryTipo.grid(column=0,row=1, sticky=W+E,padx=30, ipady=5,pady=10)
        ttk.Label(self.tab2,text="Ingrese cada elemento de su desayuno separado por un guión(-): ", style="Login.TLabel").grid(column=0,row=2, sticky=S+W,padx=35)
        self.entryDesayuno = ttk.Entry(self.tab2, width=25, justify="center", font=("Century Gothic",12));self.entryDesayuno.grid(column=0,row=3, sticky=W+E,padx=30, ipady=5,pady=10)
        ttk.Label(self.tab2,text="Ingrese cada elemento de su almuerzo separado por un guión(-): ", style="Login.TLabel").grid(column=0,row=4, sticky=S+W,padx=35)
        self.entryAlmuerzo = ttk.Entry(self.tab2, width=25, justify="center", font=("Century Gothic",12));self.entryAlmuerzo.grid(column=0,row=5, sticky=W+E,padx=30, ipady=5,pady=10)
        ttk.Label(self.tab2,text="Ingrese cada elemento de su cena separado por un guión(-): ", style="Login.TLabel").grid(column=0,row=6, sticky=S+W,padx=35)
        self.entryCena = ttk.Entry(self.tab2, width=25, justify="center", font=("Century Gothic",12));self.entryCena.grid(column=0,row=7, sticky=W+E,padx=30, ipady=5,pady=10)

        ttk.Button(self.tab1,text="Mostrar Dieta", width=20,command=lambda:self.callmostrarDieta(self.combobox.get())).grid(column=1,row=2, sticky=S+W,padx=30)
        ttk.Button(self.tab2,text="Guardar Dieta", width=20,command=lambda:self.calldatosDieta(self.entryTipo.get(),self.entryDesayuno.get(),self.entryAlmuerzo.get(),self.entryCena.get())).grid(column=0,row=8, sticky=S+W,padx=30)

    def callmostrarDieta(self, tipo):
        resultadoBusquedaTipo=self.driver.mostrarDieta(tipo)
        for index,row in resultadoBusquedaTipo.iterrows():
            etiqueta_dieta=Label(self.tab1, text=f"Tipo: {row.iloc[0]}, \nDesayuno: {row.iloc[1]}, \nAlmuerzo: {row.iloc[2]}, \nCena: {row.iloc[3]}")
            etiqueta_dieta.grid(column=0,row=3, sticky=W, padx=10, pady=5)
            etiqueta_dieta.config(bg="white",font=("Arial", 12))


    def calldatosDieta(self, tipo, desayuno, almuerzo, cena):
        try:
            self.driver.datosDieta(tipo, desayuno, almuerzo, cena)
        except:
            messagebox.showerror("Error","No ingreso algun dato")

class v_ejercicio(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        Toplevel.__init__(self)
        self.title("Ejercicios")
        self.resizable(False,False)
        self.config(bg="white")
        
        self.tab = ttk.Notebook(self)
        self.tab.grid(column=0,row=0)
        self.tab1=ttk.Frame(self.tab)
        self.tab2=ttk.Frame(self.tab)
        
        self.tab.add(self.tab1,text="Mostrar ejercicio")
        self.tab.add(self.tab2,text="Ingresar ejercicio")
        style = ttk.Style()
        style.configure("TNotebook.Tab", background="white", font=("Bahnschrift",18),foreground="#3A495B")
        style.configure("TFrame", background="white", font=("Bahnschrift",18),foreground="#3A495B")
        self.mostrarejerciciov(self.tab1)
        self.agregarejerciciov(self.tab2)
    
    def mostrarejerciciov(self,tab):
        Label(tab,text="Rutina de ejercicios", font=("HP Simplified Hans",16),bg="#3A495B",fg="white").grid(column=0,row=0, columnspan=3, sticky=W+E,pady=10,padx=30,ipady=10)
        Label(tab,text="¿Que grupo muscular desea trabajar?", font=("HP Simplified Hans",12)).grid(column=0,row=1, sticky=W+E,pady=10,padx=30,ipady=10)
        self.combobox = ttk.Combobox(tab,state="readonly",font=("HP Simplified Hans",12));self.combobox.grid(column=1,row=1, sticky=W+E,pady=10,padx=30,ipady=10)
        self.combobox['values']=tuple(self.driver.obtenerGrupo())
        self.combobox.set("Elija una opcion")
        ttk.Button(tab,text="Seleccionar", width=20,command=lambda:self.mostrar(tab,self.combobox.get())).grid(column=0,row=2,columnspan=2, sticky=W+E, padx=10,pady=30)
        self.flag = False
        self.flag2 = False
        self.lseleccion = []
        
    def mostrar(self,tab,combo):
        grupo_muscular = combo
        ejercicios = self.driver.obtenerEjercicio(grupo_muscular)
        
        if self.flag:
            self.label_frame.destroy()
        
        self.label_frame = ttk.LabelFrame(tab, text=f"Ejercicios para {grupo_muscular}")
        self.label_frame.grid(column=0, row=3, columnspan=3, sticky=W+E, pady=10, padx=30, ipady=10)
        self.vars = []

        for index, row in ejercicios.iterrows():
            var = BooleanVar()
            etiqueta_ejercicio = Checkbutton(self.label_frame, text=f"Nombre: {row.iloc[1]}, Sets: {row.iloc[2]}, Repeticiones: {row.iloc[3]}", variable=var, font=("HP Simplified Hans", 12))
            etiqueta_ejercicio.grid(column=0, row=index, sticky=W, pady=5, padx=10)
            self.vars.append(var)
        self.flag = True
        ttk.Button(tab, text="Añadir a rutina", command=lambda:self.obtener_seleccion(ejercicios,tab)).grid(column=0, row=4, pady=10)
        
    def obtener_seleccion(self,ejercicios,tab):
        seleccionados = [row[1] for var, row in zip(self.vars, ejercicios.iterrows()) if var.get()]
        self.lseleccion.extend(seleccionados)

            
        if self.flag2:
            self.label_frame2.destroy()

        self.label_frame2 = ttk.LabelFrame(tab, text=f"Rutina de ejercicios")
        self.label_frame2.grid(column=0, row=5, columnspan=3, sticky=W+E, pady=10, padx=30, ipady=10)

        label_seleccionados = Label(self.label_frame2, text="Ejercicios seleccionados:", font=("HP Simplified Hans", 12))
        label_seleccionados.grid(column=0, row=0, sticky=W, pady=5, padx=10)

        # Agregar los ejercicios seleccionados al Label
        for i, ejercicio in enumerate(self.lseleccion):
            label_ejercicio = Label(self.label_frame2, text=f"{i + 1}. {ejercicio.iloc[1]}", font=("HP Simplified Hans", 12))
            label_ejercicio.grid(column=0, row=i + 1, sticky=W, pady=5, padx=10)
        
        self.flag2 = True
        
    def agregarejerciciov(self,tab):
        Label(tab,text="Agregar ejercicio", font=("HP Simplified Hans",16),bg="#3A495B",fg="white").grid(column=0,row=0, columnspan=2, sticky=W+E,pady=10,padx=30,ipady=10)    
        Label(tab,text="Ingrese grupo muscular", font=("HP Simplified Hans",12)).grid(column=0,row=1, columnspan=2, sticky=W+E,pady=10,padx=30,ipady=10)    
        self.combobox2 = ttk.Combobox(tab,font=("HP Simplified Hans",12),width=60);self.combobox2.grid(column=0,row=2, columnspan=2, sticky=W+E,pady=10,padx=30,ipady=10)
        self.combobox2['values']=tuple(self.driver.obtenerGrupo())
        Label(tab,text="Ingrese nombre del ejercicio", font=("HP Simplified Hans",12)).grid(column=0,row=3, columnspan=2, sticky=W+E,pady=10,padx=30,ipady=10)    
        self.nombreEjercicio=ttk.Entry(tab, width=25, justify="center", font=("Century Gothic",12));self.nombreEjercicio.grid(column=0,row=4, columnspan=2, sticky=W+E,padx=30, ipady=5,pady=10)
        Label(tab,text="Ingrese sets", font=("HP Simplified Hans",12)).grid(column=0,row=5, sticky=W+E,pady=10,padx=30,ipady=10)    
        self.setsEjercicio=ttk.Entry(tab, width=5, justify="center", font=("Century Gothic",12));self.setsEjercicio.grid(column=0,row=6, sticky=W+E,padx=30, ipady=5,pady=10)
        Label(tab,text="Ingrese repeticiones", font=("HP Simplified Hans",12)).grid(column=1,row=5, sticky=W+E,pady=10,padx=30,ipady=10)    
        self.repsEjercicio=ttk.Entry(tab, width=5, justify="center", font=("Century Gothic",12));self.repsEjercicio.grid(column=1,row=6, sticky=W+E,padx=30, ipady=5,pady=10)
        ttk.Button(tab,text="Registrar", width=20, command=lambda:self.callEjercicio(self.combobox2.get(),self.nombreEjercicio.get(),
        self.setsEjercicio.get(),self.repsEjercicio.get())).grid(column=0,row=7, columnspan=2, sticky=W+E, padx=10,pady=30)
        
    def callEjercicio(self,e1,e2,e3,e4):
        try:
            self.driver.registrarEjercicio(e1,e2,e3,e4)
            messagebox.showinfo("Atencion","Se añadió con éxito")
        except Exception:
            messagebox.showerror("Error","Ingreso un dato no válido")
            
        
        
class v_tips(Toplevel):
    def __init__(self):
        self.driver = Driver.driver()
        Toplevel.__init__(self)
        self.title("Tips")
        self.resizable(False,False)
        self.config(bg="white")
        
        
        #Label(self,text="Tip 1", font=("HP Simplified Hans",16),bg="#3A495B",fg="white").grid(column=0,row=0, columnspan=3, sticky=W+E,pady=10,padx=30,ipady=10)
        #self.TIP1 = ttk.Label(self,text="TIP 1", font=("HP Simplified Hans",16), style="Login.TLabel").grid(column=0,row=0, sticky=S+W,padx=30)
        #self.TIP2 = ttk.Label(self,text="TIP 2", font=("HP Simplified Hans",16), style="Login.TLabel").grid(column=0,row=1, sticky=S+W,padx=30)
        #self.TIP3 = ttk.Label(self,text="TIP 3", font=("HP Simplified Hans",16), style="Login.TLabel").grid(column=0,row=2, sticky=S+W,padx=30)

        ttk.Button(self,text="Ver Tips", width=20,command=lambda:self.Ver_tips()).grid(column=0,row=5, sticky=S+W,padx=30)
        #self.Ver_tips()

    def Ver_tips(self):
        self.show1=self.driver.tips_ver()
        #self.show2=self.driver.tips_ver()
        #self.show3=self.driver.tips_ver()
        
        lafoto = self.show1 + ".png"

        self.fotoimagen = PhotoImage(file=lafoto)
        Label(self,image=self.fotoimagen).grid(column=0,row=1, columnspan=4,sticky=W+E)
        #self.TIP1 = ttk.Label(self,text=str(self.show1), style="Login.TLabel").grid(column=0,row=0, columnspan=2,sticky=S+W,padx=30)
        #self.TIP2 = ttk.Label(self,text=str(self.show2), style="Login.TLabel").grid(column=0,row=1, columnspan=2,sticky=S+W,padx=30)
        #self.TIP3 = ttk.Label(self,text=str(self.show3), style="Login.TLabel").grid(column=0,row=2, columnspan=2,sticky=S+W,padx=30)



app().mainloop()