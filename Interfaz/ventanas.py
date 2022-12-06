
import tkinter as tk
from tkinter.ttk import *
import funciones as fc
from tkinter import messagebox


class Win:
    def __init__(self,anch= 800, alt= 600):
        self.win= tk.Tk()
        self.win.title("Main")
        self.win.configure(background="black")
        fc.centrar(self.win,anch,alt)
        self.win.resizable(width=0, height=0)


class WinMain(Win):
    def __init__(self):
        super().__init__()
        
        
        logo= fc.imagen("Interfaz/images/carrito.png",(280,280))
        titulo= fc.imagen("Interfaz/images/logo.png",(600,150))

        frame_titulo= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, image= titulo, bg= "navy")
        etitulo.pack(side="top",fill= tk.X)
        
        frame_logo= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID)
        frame_logo.pack(side= "left", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5, ipadx= 50)
        elogo= tk.Label(frame_logo,image=logo, bg= "green yellow")
        elogo.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        
        frame_login= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID,bg= "black")
        frame_login.pack(side= "right", expand= tk.YES, fill= tk.BOTH)
        einicio= tk.Label(frame_login, text="INICIO", font= ("Times",30), fg= "black", bg= "snow4", height= 2)
        einicio.pack(side= "top",fill= tk.X, padx= 2, pady= 2)
        frame_formulario= tk.Frame(frame_login, bd= 0, width= 300, relief= tk.SOLID, bg= "light gray")
        frame_formulario.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)
        eusuario= tk.Label(frame_formulario, text= "Usuario", font= ("Times", 20), anchor= "w", bg= "light gray")
        eusuario.pack(fill= tk.X, padx= 20, pady= 5)
        self.usuario= tk.Entry(frame_formulario, font= ("Times", 20))
        self.usuario.pack(fill= tk.X, padx= 20, pady= 5)
        epassword= tk.Label(frame_formulario, text= "Contraseña", font= ("Times", 20), anchor= "w", bg= "light gray")
        epassword.pack(fill= tk.X, padx= 20, pady= 5)
        self.password= tk.Entry(frame_formulario, font= ("Times", 20))
        self.password.pack(fill= tk.X, padx= 20, pady= 5)
        self.password.config(show="*")
        binicio= tk.Button(frame_formulario,text= "Iniciar Sesion", font= ("Times", 20), bg= "dim gray", command= self.binicio)
        binicio.pack(fill= tk.X,padx= 20, pady= 20)
        bregistro= tk.Button(frame_formulario,text= "Registrar Usuario", font= ("Times", 15),bg= "light gray", bd= 0, fg= "blue", command= self.bregistro)
        bregistro.pack(fill= tk.X,padx= 20, pady= 5)

        self.win.mainloop()

    def binicio(self):
      pass

    def bregistro(self):
        pass

class WinRegistro(Win):
    def __init__(self):
        super().__init__()

        frame_titulo= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Registro", font= ("Cheddar gothic",30), bg= "snow3", fg= "Black")
        etitulo.pack(side="top",fill= tk.X)

        frame_formulario= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID, bg= "light gray")
        frame_formulario.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)
        eusuario= tk.Label(frame_formulario, text= "Usuario", font= ("Times", 15), anchor= "w", bg= "light gray")
        eusuario.pack(fill= tk.X, padx= 10, pady= 0)
        self.usuario= tk.Entry(frame_formulario, font= ("Times", 15))
        self.usuario.pack(fill= tk.X, padx= 10, pady= 0)
        epassword= tk.Label(frame_formulario, text= "Contraseña", font= ("Times", 15), anchor= "w", bg= "light gray")
        epassword.pack(fill= tk.X, padx= 10, pady= 0)
        self.password= tk.Entry(frame_formulario, font= ("Times", 15))
        self.password.pack(fill= tk.X, padx= 10, pady= 0)
        self.password.config(show="*")
        epassword2= tk.Label(frame_formulario, text= "Repita la Contraseña", font= ("Times", 15), anchor= "w", bg= "light gray")
        epassword2.pack(fill= tk.X, padx= 10, pady= 0)
        self.password2= tk.Entry(frame_formulario, font= ("Times", 15))
        self.password2.pack(fill= tk.X, padx= 10, pady= 0)
        self.password2.config(show="*")
        
        edatosp= tk.Label(frame_formulario, text= "Datos Personales", font= ("Arial", 25), bg= "light gray")
        edatosp.pack( padx= 200, pady= 5)

        enombre= tk.Label(frame_formulario, text= "Nombre", font= ("Times", 15), anchor= "w", bg= "light gray")
        enombre.pack(fill= tk.X, padx= 10, pady= 0)
        self.nombre= tk.Entry(frame_formulario, font= ("Times", 15))
        self.nombre.pack(fill= tk.X, padx= 10, pady= 0)
        eapellido= tk.Label(frame_formulario, text= "Apellido", font= ("Times", 15), anchor= "w", bg= "light gray")
        eapellido.pack(fill= tk.X, padx= 10, pady= 0)
        self.apellido= tk.Entry(frame_formulario, font= ("Times", 15))
        self.apellido.pack(fill= tk.X, padx= 10, pady= 0)
        edireccion= tk.Label(frame_formulario, text= "Direccion", font= ("Times", 15), anchor= "w", bg= "light gray")
        edireccion.pack(fill= tk.X, padx= 10, pady= 0)
        self.direccion= tk.Entry(frame_formulario, font= ("Times", 15))
        self.direccion.pack(fill= tk.X, padx= 10, pady= 0)
        email= tk.Label(frame_formulario, text= "Mail", font= ("Times", 15), anchor= "w", bg= "light gray")
        email.pack(fill= tk.X, padx= 10, pady= 0)
        self.mail= tk.Entry(frame_formulario, font= ("Times", 15))
        self.mail.pack(fill= tk.X, padx= 10, pady= 0)
        
        breg= tk.Button(frame_formulario,text= "Registrar", font= ("Times", 15), bg= "dim gray",command= self.bguardar)
        breg.pack(fill= tk.X,padx= 20, pady= 5)
        bvolver= tk.Button(frame_formulario,text= "Volver", font= ("Times", 15),bg= "dim gray",command= self.bvolver)
        bvolver.pack(fill= tk.X,padx= 20, pady= 5)

        self.win.mainloop()

    def validarMail(self):
        pass

    def validarpass(self):
        pass

    def bguardar(self):
        pass
    
    def bvolver(self):
        pass

class WinCliente(Win):
    def __init__(self):
        super().__init__(1000)

        titulo= fc.imagen("Interfaz/images/Secciones.png",(300,100))

        frame_seccion= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID, bg= "navy")
        frame_seccion.pack(side= "top", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_seccion, image= titulo, bg= "navy")
        etitulo.pack(side="left",fill= tk.X, padx= 100)

        icar= fc.imagen("Interfaz/images/carrito.png",(70,70))
        ipue= fc.imagen("Interfaz/images/salir.png",(90,70))
        bpuerta= tk.Button(frame_seccion, command= self.bsalir , image= ipue, bg= "green yellow", text= "SALIR",font= ("Arial black",15) ,compound= "top", relief= tk.RAISED, bd= 10)
        bpuerta.pack(side= "right", padx= 15)
        bcarrito= tk.Button(frame_seccion, command= self.bcarro, image= icar, bg= "green yellow", text= "CARRO",font= ("Arial black",15) ,compound= "top", relief= tk.RAISED, bd= 10)
        bcarrito.pack(side= "right", padx= 15)
        

        frame_categoria= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID, bg= "black")
        frame_categoria.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=0)

        frame_left= tk.Frame(frame_categoria, bd= 0, width= 300, relief= tk.SOLID, bg= "green yellow")
        frame_left.pack(side= "left", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)

        frame_right= tk.Frame(frame_categoria, bd= 0, width= 300, relief= tk.SOLID, bg= "green yellow")
        frame_right.pack(side= "right", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)
        

        ib1= fc.imagen("Interfaz/images/Boton1.png",(300,130))
        bsec1= tk.Button(frame_left, image= ib1, bg= "white", command= self.bot1)
        bsec1.pack(fill= tk.X,padx= 20, pady= 10)
        
        ib2= fc.imagen("Interfaz/images/Boton2.png",(300,130))
        bsec2= tk.Button(frame_left, image= ib2, bg= "white", command= self.bot2)
        bsec2.pack(fill= tk.X,padx= 20, pady= 5)

        ib3= fc.imagen("Interfaz/images/Boton3.png",(300,130))
        bsec3= tk.Button(frame_left, image= ib3, bg= "white", command= self.bot3)
        bsec3.pack(fill= tk.X,padx= 20, pady= 5)

        ib4= fc.imagen("Interfaz/images/Boton4.png",(300,130))
        bsec4= tk.Button(frame_right, image= ib4, bg= "white", command= self.bot4)
        bsec4.pack(fill= tk.X,padx= 20, pady= 10)

        ib5= fc.imagen("Interfaz/images/Boton5.png",(300,130))
        bsec5= tk.Button(frame_right, image= ib5, bg= "white", command= self.bot5)
        bsec5.pack(fill= tk.X,padx= 20, pady= 5)
        
        ib6= fc.imagen("Interfaz/images/Boton6.png",(300,130))
        bsec6= tk.Button(frame_right, image= ib6, bg= "white", command= self.bot6)
        bsec6.pack(fill= tk.X,padx= 20, pady= 5)
        
        self.win.mainloop()

    
    def bot1(self):        
        pass

    def bot2(self):        
        pass

    def bot3(self):        
        pass

    def bot4(self):        
        pass

    def bot5(self):        
        pass

    def bot6(self):        
        pass

    def bcarro(self):
        pass

    def bsalir(self):
        pass

class WinPersonal(Win):
    def __init__(self):
        super().__init__(1000)
        

        titulo= fc.imagen("Interfaz/images/administracion.png",(600,100))

        frame_almacen= tk.Frame(self.win, bd= 0, width= 100, relief= tk.SOLID, bg= "gray")
        frame_almacen.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_almacen, image= titulo, bg= "gray")
        etitulo.pack(fill= tk.X, padx= 100)
       
        frame_menu= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID, bg= "navy")
        frame_menu.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=0)

        icar= fc.imagen("Interfaz/images/cargar.png",(100,70))
        imod= fc.imagen("Interfaz/images/modificar.png",(100,70))
        ilist= fc.imagen("Interfaz/images/lista.png",(100,70))
        isalir= fc.imagen("Interfaz/images/salir.png",(100,70))

        bcargar= tk.Button(frame_menu,command= self.btcar, image= icar, text= "   Cargar Producto", font= ("Times", 30), bg= "dim gray", compound= "left", bd= 10)
        bcargar.pack(fill= tk.X,padx= 100, pady= 20)

        bmodificar= tk.Button(frame_menu, command= self.btmodi, image= imod,text= "  Modificar Producto", font= ("Times", 30), bg= "dim gray", compound= "left", bd= 10)
        bmodificar.pack(fill= tk.X,padx= 100, pady= 10)

        blistar= tk.Button(frame_menu,command= self.btlistar, image= ilist, text= "  Listar Clientes", font= ("Times", 30), bg= "dim gray", compound= "left", bd= 10)
        blistar.pack(fill= tk.X,padx= 100, pady= 10)

        bsalir= tk.Button(frame_menu, command= self.btsalir, image= isalir, text= " Salir", font= ("Times", 30), bg= "dim gray", compound= "left", bd= 10)
        bsalir.pack(fill= tk.X,padx= 100, pady= 10)

        self.win.mainloop()

    def btcar(self):
        pass

    def btmodi(self):
        pass

    def btlistar(self):
        pass

    def btsalir(self):
        pass

class WinCarga(Win):
    def __init__(self):
        super().__init__()
        
        
        frame_titulo= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Cargar Producto", font= ("Cheddar gothic",30), bg= "snow3", fg= "Black")
        etitulo.pack(side="top",fill= tk.X)

        frame_formulario= tk.Frame(self.win, bd= 0, width= 300, relief= tk.SOLID, bg= "navy")
        frame_formulario.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)
        frame_left= tk.Frame(frame_formulario, bd= 0, width= 300, relief= tk.SOLID, bg= "navy")
        frame_left.pack(side= "left", expand= tk.YES, fill= tk.BOTH, padx=5, pady=15)
        frame_right= tk.Frame(frame_formulario, bd= 0, width= 300, relief= tk.SOLID, bg= "navy")
        frame_right.pack(side= "right", expand= tk.YES, fill= tk.BOTH, padx=5, pady=15)
        eid= tk.Label(frame_left, text= "ID Producto", font= ("Times", 25), bg= "navy", fg= "white")
        eid.pack(fill= tk.BOTH, padx= 10, pady= 20)
        self.id= tk.Entry(frame_right, font= ("Times", 25))
        self.id.pack(fill= tk.BOTH, padx= 10, pady= 20)
        enombre= tk.Label(frame_left, text= "Nombre Producto", font= ("Times", 25), bg= "navy", fg= "white")
        enombre.pack(fill= tk.BOTH, padx= 10, pady= 20)
        self.nombre= tk.Entry(frame_right, font= ("Times", 25))
        self.nombre.pack(fill= tk.BOTH, padx= 10, pady= 20)
        ecategoria= tk.Label(frame_left, text= "Categoria", font= ("Times", 25), bg= "navy", fg= "white")
        ecategoria.pack(fill= tk.BOTH, padx= 10, pady= 20)
        self.categoria= Combobox(frame_right, font= ("Times", 25), state= "readonly", values= ["Bebidas", "Congelados","Cuidado Personal", "Despensa", "Limpieza", "Refrigerados"])
        self.categoria.pack(fill= tk.BOTH, padx= 10, pady= 20)
        estock= tk.Label(frame_left, text= "Stock Producto", font= ("Times", 25), bg= "navy", fg= "white")
        estock.pack(fill= tk.BOTH, padx= 10, pady= 20)
        self.stock= tk.Entry(frame_right, font= ("Times", 25))
        self.stock.pack(fill= tk.BOTH, padx= 10, pady= 20)
        eprecio= tk.Label(frame_left, text= "Precio Producto", font= ("Times", 30), bg= "navy", fg= "white")
        eprecio.pack(fill= tk.BOTH, padx= 10, pady= 20)
        self.precio= tk.Entry(frame_right, font= ("Times", 25))
        self.precio.pack(fill= tk.BOTH, padx= 10, pady= 20)

        bvolver= tk.Button(frame_left, command= self.bvolver, text= "Volver", font= ("Times", 15),bg= "dim gray")
        bvolver.pack(fill= tk.X,padx= 20, pady= 5, side= "bottom")        
        bguardar= tk.Button(frame_right, command= self.bguardar,text= "Guardar", font= ("Times", 15), bg= "dim gray")
        bguardar.pack(fill= tk.X,padx= 20, pady= 5, side= "bottom")
        

        self.win.mainloop()

    def bvolver(self):
        pass

    def bguardar(self):
        pass

class WinModpro(Win):
    def __init__(self):
        super().__init__()
        

        frame_titulo= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Modificar Producto", font= ("Cheddar gothic",30), bg= "snow3", fg= "Black")
        etitulo.pack(side="top",fill= tk.X)
        frame_tree= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_tree.pack(expand= tk.YES, fill= tk.BOTH, padx=50, pady=15)
        self.tabla= Treeview(frame_tree, columns= ("#1","#2", "#3", "#4", "#5" ),height= 12,)
        self.tabla.grid(row= 2, column= 0, columnspan= 4)
        self.tabla.bind("<Double-Button-1>",self.dctabla)
        self.tabla["show"]= "headings"
        self.tabla.heading("#1", text= "ID", anchor= tk.CENTER)
        self.tabla.heading("#2", text= "Nombre", anchor= tk.CENTER)
        self.tabla.heading("#3", text= "Categoria", anchor= tk.CENTER)
        self.tabla.heading("#4", text= "Stock", anchor= tk.CENTER)
        self.tabla.heading("#5", text= "Precio", anchor= tk.CENTER)
        self.tabla.column("#1", width= 50,anchor= tk.CENTER)
        self.tabla.column("#2", width= 280,anchor= tk.CENTER)
        self.tabla.column("#3", width= 200,anchor= tk.CENTER)
        self.tabla.column("#4", width= 50,anchor= tk.CENTER)
        self.tabla.column("#5", width= 100,anchor= tk.CENTER)
        scrollbar = Scrollbar(frame_tree, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=4, sticky='ns')
        frame_controles= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "black")
        frame_controles.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)

        enombre= tk.Label(frame_controles, text= "Nombre Producto", font= ("Times", 18), bg= "black", fg= "white")
        enombre.grid(row=0, column= 0,padx= 30 )
        self.nombre= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.nombre.grid(row= 0, column= 1, pady= 20, padx=50)
        ecategoria= tk.Label(frame_controles, text= "Categoria", font= ("Times", 18), bg= "black", fg= "white")
        ecategoria.grid(row= 1, column= 0)
        self.categoria= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.categoria.grid(row= 1, column= 1)
        estock= tk.Label(frame_controles, text= "Stock Producto", font= ("Times", 18), bg= "black", fg= "white")
        estock.grid(row= 2, column= 0)
        self.stock= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.stock.grid(row= 2, column= 1, pady= 20)
        eprecio= tk.Label(frame_controles, text= "Precio Producto", font= ("Times", 18), bg= "black", fg= "white")
        eprecio.grid(row= 3, column= 0)
        self.precio= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.precio.grid(row= 3, column= 1)

        self.bmodificar= tk.Button(frame_controles, command= self.bmod, text= "Modificar", font= ("Times", 15),bg= "yellow", bd= 5)
        self.bmodificar.grid(row= 0, column= 2, padx= 20)    
        self.bmodificar["state"]= "disable"    
        self.bborr= tk.Button(frame_controles, command= self.bborrar, text= "Borrar", font= ("Times", 15), bg= "red", bd= 5)
        self.bborr.grid(row= 1, column= 2)
        self.bborr["state"]= "disable"
        bvolver= tk.Button(frame_controles, command= self.bvol, text= "Volver", font= ("Times", 15), bg= "dim gray", bd= 5)
        bvolver.grid(row= 2, column= 2)

        self.db= fc.conexion("supermark.db")
        self.db.mostrartree(self.tabla, """SELECT "id", "nombre", "categoria", "cantidad", "precio" FROM "almacen" """)

        self.win.mainloop()

    
    def dctabla(self, event):
        pass
        
    def bmod(self):
        pass

    def bborrar(self):
        pass
    
    def bvol(self):
        pass

class WinListaClientes(Win):
    def __init__(self):
        super().__init__()
        
        frame_titulo= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Lista Clientes", font= ("Cheddar gothic",30), bg= "snow3", fg= "Black")
        etitulo.pack(side="top",fill= tk.X)
        frame_tree= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_tree.pack(expand= tk.YES, fill= tk.BOTH, padx=50, pady=15)
        self.tabla= Treeview(frame_tree, columns= ("#1","#2", "#3", "#4", "#5", "#6" ),height= 11, padding= 12 )
        self.tabla.grid(row= 2, column= 0, columnspan= 4)
        self.estilo= Style()
        self.estilo.theme_use("clam")
        self.estilo.map("Treeview", background=[("selected","navy")])
        self.tabla.bind("<Double-Button-1>",self.dctabla)
        self.tabla["show"]= "headings"
        self.tabla.heading("#1", text= "User", anchor= tk.CENTER)
        self.tabla.heading("#2", text= "Nombre", anchor= tk.CENTER)
        self.tabla.heading("#3", text= "Apellido", anchor= tk.CENTER)
        self.tabla.heading("#4", text= "Mail", anchor= tk.CENTER)
        self.tabla.heading("#5", text= "Direccion", anchor= tk.CENTER)
        self.tabla.heading("#6", text= "Carro", anchor= tk.CENTER)
        self.tabla.column("#1", width= 48,anchor= tk.CENTER)
        self.tabla.column("#2", width= 140,anchor= tk.CENTER)
        self.tabla.column("#3", width= 140,anchor= tk.CENTER)
        self.tabla.column("#4", width= 140,anchor= tk.CENTER)
        self.tabla.column("#5", width= 140,anchor= tk.CENTER)
        self.tabla.column("#6", width= 50,anchor= tk.CENTER)
        scrollbar = Scrollbar(frame_tree, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=4, sticky='ns')
        frame_controles= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "black")
        frame_controles.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)

        enombre= tk.Label(frame_controles, text= "Nombre Cliente", font= ("Times", 18), bg= "black", fg= "white")
        enombre.grid(row=0, column= 0,padx= 30 )
        self.nombre= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.nombre.grid(row= 0, column= 1, pady= 10, padx=50)
        eapellido= tk.Label(frame_controles, text= "Apellido", font= ("Times", 18), bg= "black", fg= "white")
        eapellido.grid(row= 1, column= 0)
        self.apellido= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.apellido.grid(row= 1, column= 1)
        email= tk.Label(frame_controles, text= "E-Mail", font= ("Times", 18), bg= "black", fg= "white")
        email.grid(row= 2, column= 0)
        self.mail= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.mail.grid(row= 2, column= 1, pady= 10)
        edireccion= tk.Label(frame_controles, text= "Direccion", font= ("Times", 18), bg= "black", fg= "white")
        edireccion.grid(row= 3, column= 0)
        self.direccion= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.direccion.grid(row= 3, column= 1)

        self.bmodificar= tk.Button(frame_controles, command= self.bmod, text= "Modificar", font= ("Times", 12),bg= "yellow", bd= 5)
        self.bmodificar.grid(row= 0, column= 2, padx= 5)    
        self.bmodificar["state"]= "disable"    
        self.bborr= tk.Button(frame_controles, command= self.bborrar, text= "Borrar", font= ("Times", 12), bg= "red", bd= 5)
        self.bborr.grid(row= 1, column= 2)
        self.bborr["state"]= "disable"
        self.bcarro= tk.Button(frame_controles, command= self.btcarro, text= "Carro", font= ("Times", 12), bg= "navy", fg= "white", bd= 5)
        self.bcarro.grid(row= 2, column= 2)
        self.bcarro["state"]= "disable"
        self.bpedidos= tk.Button(frame_controles, command= self.bfpedido, text= "Pedidos", font= ("Times", 12), bg= "navy", fg= "white", bd= 5)
        self.bpedidos.grid(row= 2, column= 3)
        bvolver= tk.Button(frame_controles, command= self.bvol, text= "Volver", font= ("Times", 12), bg= "dim gray", bd= 5)
        bvolver.grid(row= 3, column= 2)

        self.db= fc.conexion("supermark.db")
        self.db.mostrartree(self.tabla, """SELECT "usuario", "nombre", "apellido", "mail", "direccion", "pedido" FROM "cliente" """)

        self.win.mainloop()

    def dctabla(self, event):
        pass
        
    def bmod(self): 
        pass

    def bborrar(self):
        pass

    def btcarro(self):        
        pass

    def bfpedido(self):
        pass
    
    def bvol(self):
        pass  

class WinSecciones(Win):
    def __init__(self, categoria):
        super().__init__()
        
        
        frame_titulo= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= f"{categoria}", font= ("Cheddar gothic",30), bg= "navy", fg= "red")
        etitulo.pack(side="top",fill= tk.X)
        frame_tree= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_tree.pack(expand= tk.YES, fill= tk.BOTH, padx=50, pady=20)
        self.estilo= Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("Treeview", background= "green yellow",fieldbackground= "green yellow" , font= ("Cheddar gothic",15), rowheight= 20)
        self.estilo.map("Treeview", background=[("selected","navy")])
        self.tabla= Treeview(frame_tree, columns= ("#1","#2", "#3"),height= 12,)
        self.tabla.grid(row= 2, column= 0, columnspan= 3)
        self.tabla.bind("<Double-Button-1>",self.dctabla)
        self.tabla["show"]= "headings"
        self.tabla.heading("#1", text= "ID", anchor= tk.CENTER)
        self.tabla.heading("#2", text= "Nombre Producto", anchor= tk.CENTER)
        self.tabla.heading("#3", text= "Precio", anchor= tk.CENTER)
        self.tabla.column("#1", width= 50,anchor= tk.CENTER)
        self.tabla.column("#2", width= 380,anchor= tk.CENTER)
        self.tabla.column("#3", width= 250,anchor= tk.CENTER)
        scrollbar = Scrollbar(frame_tree, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=4, sticky='ns')
        frame_controles= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "navy")
        frame_controles.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)

        enombre= tk.Label(frame_controles, text= "Nombre Producto", font= ("Times", 18), bg= "navy", fg= "white")
        enombre.grid(row=0, column= 0,padx= 30 )
        self.nombre= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.nombre.grid(row= 0, column= 1, pady= 15, padx=50)
        ecantidad= tk.Label(frame_controles, text= "Cantidad", font= ("Times", 18), bg= "navy", fg= "white")
        ecantidad.grid(row= 2, column= 0)
        self.precio= tk.Entry(frame_controles, font= ("Times", 18), width= 25, justify= tk.CENTER)
        self.precio.grid(row= 1, column= 1)
        eprecio= tk.Label(frame_controles, text= "Precio", font= ("Times", 18), bg= "navy", fg= "white")
        eprecio.grid(row= 1, column= 0)
        self.cantidad= tk.Spinbox(from_=1, to= 50, font= ("Times", 18), command= self.ftotal, justify= tk.CENTER )
        self.cantidad.place(x=293, y=505, width= 305, height= 30)
        self.cantidad.delete(0, tk.END)
        etotal= tk.Label(frame_controles, text= "Total", font= ("Times", 18), bg= "navy", fg= "white")
        etotal.grid(row= 3, column= 0)
        self.total= tk.Entry(frame_controles, font= ("Times", 18), width= 25, justify= tk.CENTER)
        self.total.grid(row= 3, column= 1)
        self.cantidad["state"]= "readonly"
        self.total["state"]= "readonly"
        self.nombre["state"]= "readonly"
        self.precio["state"]= "readonly"

        self.bagregar= tk.Button(frame_controles, command= self.bfagregar, text= "Agregar", font= ("Times", 15), bg= "green", bd= 5, fg= "white")
        self.bagregar.grid(row= 0, column= 2)
        self.bagregar["state"]= "disable"
        self.bcarro= tk.Button(frame_controles, command= self.bfcarro, text= "Carro", font= ("Times", 15), bg= "yellow", bd= 5)
        self.bcarro.grid(row= 1, column= 2, pady= 5)
        bvolver= tk.Button(frame_controles, command= self.bfvol, text= "Volver", font= ("Times", 15), bg= "dim gray", bd= 5)
        bvolver.grid(row= 2, column= 2 )
        self.info= tk.Label(self.win, text="Info: Seleccione con doble click el Producto y luego Ajuste la cantidad deseada", font=("Arial Black",10),anchor= tk.W, bg= "gray")
        self.info.place(y= 360, x= 5,width= 790)

        self.db= fc.conexion("supermark.db")
        self.db.mostrartree(self.tabla, f"""SELECT "id", "nombre", "precio" FROM "almacen" WHERE categoria="{categoria}" and cantidad > 0""")

        self.win.mainloop()
    
    def dctabla(self, event):
        pass

    def ftotal(self):
        pass

    def bfagregar(self):
        pass
        
    def bfcarro(self):
        pass
    
    def bfvol(self):
        pass

class WinCarro(Win):
    def __init__(self):
        super().__init__()

        frame_titulo= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "CARRO", font= ("Cheddar gothic",30), bg= "navy", fg= "red")
        etitulo.pack(side="top",fill= tk.X)
        frame_left= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "gray")
        frame_left.pack(side= "left", expand= tk.NO, fill= tk.Y, padx=5, pady=5)
        frame_right= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "green yellow")
        frame_right.pack(side= "right", expand= tk.NO, fill= tk.Y, padx=5, pady=5)

        self.estilo= Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("Treeview", background= "green yellow",fieldbackground= "green yellow" , font= ("Cheddar gothic",12), rowheight= 20)
        self.estilo.map("Treeview", background=[("selected","navy")])
        self.tabla= Treeview(frame_left, columns= ("#1","#2", "#3", "#4", "#5" ),height= 11, padding= 12 )
        self.tabla.grid(row=2, column=0, ipady= 128, )
        self.tabla.bind("<Double-Button-1>",self.dctabla)
        self.tabla["show"]= "headings"
        self.tabla.heading("#1", text= "#", anchor= tk.CENTER)
        self.tabla.heading("#2", text= "Producto", anchor= tk.CENTER)
        self.tabla.heading("#3", text= "Precio", anchor= tk.CENTER)
        self.tabla.heading("#4", text= "Cantidad", anchor= tk.CENTER)
        self.tabla.heading("#5", text= "Total", anchor= tk.CENTER)
        self.tabla.column("#1", width= 20,anchor= tk.CENTER)
        self.tabla.column("#2", width= 270,anchor= tk.CENTER)
        self.tabla.column("#3", width= 80,anchor= tk.CENTER)
        self.tabla.column("#4", width= 50,anchor= tk.CENTER)
        self.tabla.column("#5", width= 100,anchor= tk.CENTER)
        scrollbar = Scrollbar(frame_left, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=5, sticky='ns')

        etotal= tk.Label(frame_right, text= "TOTAL", font= ("Arial Black", 30), bg= "green yellow")
        etotal.pack(pady= 25)
        self.total= tk.Entry(frame_right, font= ("Arial Black", 25), justify= tk.CENTER)
        self.total.pack(padx= 30)
        self.total["state"]= "readonly"

        self.bfinalizar= tk.Button(frame_right, command= self.bffinalizar, text= "Realizar Pedido", font= ("Times", 15), bg= "green", bd= 5, fg= "white")
        self.bfinalizar.pack(pady= 30)
        self.bcancelar= tk.Button(frame_right, command= self.bfcancelar, text= "Cancelar Pedido", font= ("Times", 15), bg= "red", bd= 5, fg= "white")
        self.bcancelar.pack(pady= 10)
        self.bquitar= tk.Button(frame_right, command= self.bfquitar, text= "Quitar", font= ("Times", 15), bg= "red", bd= 5, fg= "white")
        self.bquitar.pack(pady= 10)
        self.bquitar["state"]= "disabled"
        self.bcancelar["state"]= "disabled"
        self.bvolver= tk.Button(frame_right, command= self.bfvolver, text= "Volver", font= ("Times", 15), bg= "green", bd= 5, fg= "white")
        self.bvolver.pack(pady= 10)

        self.db= fc.conexion("supermark.db")
        self.mostrar()
        self.ftotal()

        self.win.mainloop()

    def mostrar(self):
        pass

    def dctabla(self, event):
        pass

    def ftotal(self):
        pass

    def bffinalizar(self):
        pass

    def bfcancelar(self):
        pass

    def bfquitar(self):
        pass

    def bfvolver(self):
        pass

class WinCarroAdmin(Win):
    def __init__(self, user):
        super().__init__()

        self.user = user
        frame_titulo= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "CARRO", font= ("Cheddar gothic",30), bg= "snow3", fg= "black")
        etitulo.pack(side="top",fill= tk.X)
        frame_left= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "gray")
        frame_left.pack(side= "left", expand= tk.NO, fill= tk.Y, padx=5, pady=5)
        frame_right= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "black")
        frame_right.pack(side= "right", expand= tk.NO, fill= tk.Y, padx=5, pady=5)

        self.estilo= Style()
        self.estilo.theme_use("clam")
        self.estilo.map("Treeview", background=[("selected","navy")])
        self.tabla= Treeview(frame_left, columns= ("#1","#2", "#3", "#4", "#5" ),height= 11, padding= 12 )
        self.tabla.grid(row=2, column=0, ipady= 128, )
        self.tabla["show"]= "headings"
        self.tabla.heading("#1", text= "#", anchor= tk.CENTER)
        self.tabla.heading("#2", text= "Producto", anchor= tk.CENTER)
        self.tabla.heading("#3", text= "Precio", anchor= tk.CENTER)
        self.tabla.heading("#4", text= "Cantidad", anchor= tk.CENTER)
        self.tabla.heading("#5", text= "Total", anchor= tk.CENTER)
        self.tabla.column("#1", width= 20,anchor= tk.CENTER)
        self.tabla.column("#2", width= 270,anchor= tk.CENTER)
        self.tabla.column("#3", width= 80,anchor= tk.CENTER)
        self.tabla.column("#4", width= 50,anchor= tk.CENTER)
        self.tabla.column("#5", width= 100,anchor= tk.CENTER)
        scrollbar = Scrollbar(frame_left, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=5, sticky='ns')

        etotal= tk.Label(frame_right, text= "TOTAL", font= ("Arial Black", 30), bg= "black", fg= "white")
        etotal.pack(pady= 25)
        self.total= tk.Entry(frame_right, font= ("Arial Black", 25), justify= tk.CENTER)
        self.total.pack(padx= 30)
        self.total["state"]= "readonly"

        self.bfinalizar= tk.Button(frame_right, command= self.bfenviar, text= "Finalizar", font= ("Times", 20), bg= "green", bd= 5, fg= "white")
        self.bfinalizar.pack(pady= 35)
        self.bvolver= tk.Button(frame_right, command= self.bfvolver, text= "Volver", font= ("Times", 20), bg= "dim grey", bd= 5, fg= "black")
        self.bvolver.pack(pady= 20)

        self.db= fc.conexion("supermark.db")
        self.mostrar()
        self.ftotal()

        self.win.mainloop()  

    def mostrar(self):
        pass
    
    def ftotal(self):
        pass

    def bfenviar(self):
        pass

    def bfvolver(self):
        pass

class WinListaPedidos(Win):
    def __init__(self):
        super().__init__()

        frame_titulo= tk.Frame(self.win, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Lista de Pedidos", font= ("Cheddar gothic",30), bg= "snow3", fg= "black")
        etitulo.pack(side="top",fill= tk.X)
        frame_mid= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "gray")
        frame_mid.pack(expand= tk.NO, fill= tk.Y, padx=5, pady=5)
        frame_bot= tk.Frame(self.win, bd= 0, relief= tk.SOLID, bg= "black")
        frame_bot.pack(side= "right", expand= tk.NO, fill= tk.Y, padx=5, pady=5)

        self.estilo= Style()
        self.estilo.theme_use("clam")
        self.estilo.map("Treeview", background=[("selected","navy")])
        self.tabla= Treeview(frame_mid, columns= ("#1","#2", "#3", "#4", "#5", "#6", "#7"  ),height= 11, padding= 12 )
        self.tabla.grid(row=2, column=0, ipady= 100, )
        self.tabla["show"]= "headings"
        self.tabla.heading("#1", text= "id", anchor= tk.CENTER)
        self.tabla.heading("#2", text= "Fecha Pedido", anchor= tk.CENTER)
        self.tabla.heading("#3", text= "Hora Pedido", anchor= tk.CENTER)
        self.tabla.heading("#4", text= "Usuario", anchor= tk.CENTER)
        self.tabla.heading("#5", text= "Total", anchor= tk.CENTER)
        self.tabla.heading("#6", text= "Fecha Entrega", anchor= tk.CENTER)
        self.tabla.heading("#7", text= "Hora Entrega", anchor= tk.CENTER)
        self.tabla.column("#1", width= 20,anchor= tk.CENTER)
        self.tabla.column("#2", width= 100,anchor= tk.CENTER)
        self.tabla.column("#3", width= 100,anchor= tk.CENTER)
        self.tabla.column("#4", width= 100,anchor= tk.CENTER)
        self.tabla.column("#5", width= 100,anchor= tk.CENTER)
        self.tabla.column("#6", width= 100,anchor= tk.CENTER)
        self.tabla.column("#7", width= 100,anchor= tk.CENTER)
        scrollbar = Scrollbar(frame_mid, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=8, sticky='ns')

        self.bvolver= tk.Button(frame_bot, command= self.bfvolver, text= "Volver", font= ("Times", 20), bg= "dim grey", bd= 5, fg= "black")
        self.bvolver.pack()

        self.db= fc.conexion("supermark.db")
        self.mostrar()
        

        self.win.mainloop()  

    def mostrar(self):
        pass

    def bfvolver(self):
        pass


        
              
        
        
    



        


        
     


