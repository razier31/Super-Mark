import tkinter as tk
from tkinter.ttk import *
import funciones as fc
from tkinter import messagebox





class Main():
    def __init__(self):
        self.mainwin= tk.Tk()
        self.mainwin.title("Main")
        self.mainwin.configure(background="black")
        fc.centrar(self.mainwin,800,600)
        self.mainwin.resizable(width=0, height=0)
        
        logo= fc.imagen("images/carrito.png",(280,280))
        titulo= fc.imagen("images/logo.png",(600,150))

        frame_titulo= tk.Frame(self.mainwin, bd= 0, width= 300, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, image= titulo, bg= "navy")
        etitulo.pack(side="top",fill= tk.X)
        
        frame_logo= tk.Frame(self.mainwin, bd= 0, width= 300, relief= tk.SOLID)
        frame_logo.pack(side= "left", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5, ipadx= 50)
        elogo= tk.Label(frame_logo,image=logo, bg= "green yellow")
        elogo.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        
        frame_login= tk.Frame(self.mainwin, bd= 0, width= 300, relief= tk.SOLID,bg= "black")
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
        
        self.mainwin.mainloop()

    def binicio(self):
        bd= fc.conexion("supermark.db")
        us= bd.validar(f"SELECT usuario FROM user WHERE usuario= '{self.usuario.get()}'")
        ps= bd.validar(f"SELECT pass FROM user WHERE pass= '{self.password.get()}' and usuario= '{self.usuario.get()}'")
        ad= bd.validar(f"SELECT admin FROM user WHERE admin= 'si' and usuario= '{self.usuario.get()}'")
        if  us  and ps:
            if ad :
                bd.cerrar()
                self.mainwin.destroy()
                WinPersonal()
            else:
                bd.cerrar()
                self.mainwin.destroy()
                WinCliente()
        else:
            messagebox.showerror(message= "La contraseña o el usuario es Incorrecto", title= "Mensaje")

    def bregistro(self):
        self.mainwin.destroy()
        Registro()

class Registro:
    def __init__(self):
        self.registro= tk.Tk()
        self.registro.title("Registro")
        self.registro.configure(background="black")
        fc.centrar(self.registro,800,600)
        self.registro.resizable(width=0, height=0)

        frame_titulo= tk.Frame(self.registro, bd= 0, width= 300, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Registro", font= ("Cheddar gothic",30), bg= "snow3", fg= "Black")
        etitulo.pack(side="top",fill= tk.X)

        frame_formulario= tk.Frame(self.registro, bd= 0, width= 300, relief= tk.SOLID, bg= "light gray")
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

        self.registro.mainloop()

    def validarMail(self):
        if "@" in self.mail.get() and "." in self.mail.get():
            return True
        else:
            messagebox.showerror(message= "El formato de Email es Incorrecto", title= "Mensaje")
            return False

    def validarpass(self):
        if self.password.get() == self.password2.get():
            return True
        else:
            messagebox.showerror(message= "La contraseña no coincide", title= "Mensaje")
            return False

    def bguardar(self):
        if self.validarMail() and self.validarpass():
            db= fc.conexion("supermark.db")
            try:
                db.consulta(f"""INSERT INTO user VALUES("{self.usuario.get()}","{self.password.get()}","no")""")
                db.consulta(f"""INSERT INTO cliente VALUES(null,"{self.nombre.get()}","{self.apellido.get()}","{self.mail.get()}","{self.direccion.get()}","{self.usuario.get()}","no")""")
                db.commit()
                messagebox.showinfo(title= "Informacion", message="Registro Exitoso")
                self.registro.destroy()
                Main()
            except:
                messagebox.showerror(message= "El nombre de usuario ya Existe", title= "Mensaje")
            db.cerrar()

    
    def bvolver(self):
        self.registro.destroy()
        Main()

class WinCliente:
    def __init__(self):
        self.wincliente= tk.Tk()
        self.wincliente.title("Cliente")
        self.wincliente.configure(background="black")
        fc.centrar(self.wincliente,1000,600)
        self.wincliente.resizable(width=0, height=0)

        titulo= fc.imagen("images/Secciones.png",(300,100))

        frame_seccion= tk.Frame(self.wincliente, bd= 0, width= 300, relief= tk.SOLID, bg= "navy")
        frame_seccion.pack(side= "top", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_seccion, image= titulo, bg= "navy")
        etitulo.pack(side="left",fill= tk.X, padx= 100)

        icar= fc.imagen("images/carrito.png",(70,70))
        ipue= fc.imagen("images/salir.png",(90,70))
        bcarrito= tk.Button(frame_seccion, image= ipue, bg= "green yellow", text= "SALIR",font= ("Arial black",15) ,compound= "top", relief= tk.RAISED, bd= 10)
        bcarrito.pack(side= "right", padx= 15)
        bcarrito= tk.Button(frame_seccion, image= icar, bg= "green yellow", text= "CARRO",font= ("Arial black",15) ,compound= "top", relief= tk.RAISED, bd= 10)
        bcarrito.pack(side= "right", padx= 15)
        

        frame_categoria= tk.Frame(self.wincliente, bd= 0, width= 300, relief= tk.SOLID, bg= "black")
        frame_categoria.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=0)

        frame_left= tk.Frame(frame_categoria, bd= 0, width= 300, relief= tk.SOLID, bg= "green yellow")
        frame_left.pack(side= "left", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)

        frame_right= tk.Frame(frame_categoria, bd= 0, width= 300, relief= tk.SOLID, bg= "green yellow")
        frame_right.pack(side= "right", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)
        

        ib1= fc.imagen("images/Boton1.png",(300,130))
        bsec1= tk.Button(frame_left, image= ib1, bg= "white", command= self.bot1)
        bsec1.pack(fill= tk.X,padx= 20, pady= 10)
        
        ib2= fc.imagen("images/Boton2.png",(300,130))
        bsec2= tk.Button(frame_left, image= ib2, bg= "white")
        bsec2.pack(fill= tk.X,padx= 20, pady= 5)

        ib3= fc.imagen("images/Boton3.png",(300,130))
        bsec3= tk.Button(frame_left, image= ib3, bg= "white")
        bsec3.pack(fill= tk.X,padx= 20, pady= 5)

        ib4= fc.imagen("images/Boton4.png",(300,130))
        bsec4= tk.Button(frame_right, image= ib4, bg= "white")
        bsec4.pack(fill= tk.X,padx= 20, pady= 10)

        ib5= fc.imagen("images/Boton5.png",(300,130))
        bsec5= tk.Button(frame_right, image= ib5, bg= "white")
        bsec5.pack(fill= tk.X,padx= 20, pady= 5)
        
        ib6= fc.imagen("images/Boton6.png",(300,130))
        bsec6= tk.Button(frame_right, image= ib6, bg= "white")
        bsec6.pack(fill= tk.X,padx= 20, pady= 5)
        
        self.wincliente.mainloop()

    def bot1(self):
        pass

class WinPersonal:
    def __init__(self):
        self.winpersonal= tk.Tk()
        self.winpersonal.title("Personal")
        self.winpersonal.configure(background="black")
        fc.centrar(self.winpersonal,1000,600)
        self.winpersonal.resizable(width=0, height=0)

        titulo= fc.imagen("images/administracion.png",(600,100))

        frame_almacen= tk.Frame(self.winpersonal, bd= 0, width= 100, relief= tk.SOLID, bg= "gray")
        frame_almacen.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_almacen, image= titulo, bg= "gray")
        etitulo.pack(fill= tk.X, padx= 100)
       
        frame_menu= tk.Frame(self.winpersonal, bd= 0, width= 300, relief= tk.SOLID, bg= "navy")
        frame_menu.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=0)

        icar= fc.imagen("images/cargar.png",(100,70))
        imod= fc.imagen("images/modificar.png",(100,70))
        ilist= fc.imagen("images/lista.png",(100,70))
        isalir= fc.imagen("images/salir.png",(100,70))

        bcargar= tk.Button(frame_menu,command= self.btcar, image= icar, text= "   Cargar Producto", font= ("Times", 30), bg= "dim gray", compound= "left", bd= 10)
        bcargar.pack(fill= tk.X,padx= 100, pady= 20)

        bmodificar= tk.Button(frame_menu, command= self.btmodi, image= imod,text= "  Modificar Producto", font= ("Times", 30), bg= "dim gray", compound= "left", bd= 10)
        bmodificar.pack(fill= tk.X,padx= 100, pady= 10)

        blistar= tk.Button(frame_menu, image= ilist, text= "  Listar Clientes", font= ("Times", 30), bg= "dim gray", compound= "left", bd= 10)
        blistar.pack(fill= tk.X,padx= 100, pady= 10)

        bsalir= tk.Button(frame_menu, image= isalir, text= " Salir", font= ("Times", 30), bg= "dim gray", compound= "left", bd= 10)
        bsalir.pack(fill= tk.X,padx= 100, pady= 10)

        self.winpersonal.mainloop()

    def btcar(self):
        self.winpersonal.destroy()
        WinCarga("Admin01")

    def btmodi(self):
        self.winpersonal.destroy()
        WinModpro("Admin01")

class WinCarga:
    def __init__(self, pkey):
        self.pkey= pkey
        self.carga= tk.Tk()
        self.carga.title("Cargar Productos")
        self.carga.configure(background="black")
        fc.centrar(self.carga,800,600)
        self.carga.resizable(width=0, height=0)

        frame_titulo= tk.Frame(self.carga, bd= 0, width= 300, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Cargar Producto", font= ("Cheddar gothic",30), bg= "snow3", fg= "Black")
        etitulo.pack(side="top",fill= tk.X)

        frame_formulario= tk.Frame(self.carga, bd= 0, width= 300, relief= tk.SOLID, bg= "navy")
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
        

        self.carga.mainloop()

    def bvolver(self):
        self.carga.destroy()
        WinPersonal()

    def bguardar(self):
        db= fc.conexion("supermark.db")
        try:
            db.consulta(f"""INSERT INTO almacen VALUES("{self.id.get()}","{self.nombre.get()}","{self.categoria.get()}","{self.stock.get()}","{self.precio.get()}","{self.pkey}")""")
            db.commit()
            messagebox.showinfo(title= "Informacion", message="Producto Guardado")
              
        except:
            messagebox.showerror(message= "El ID del Producto ya Existe", title= "Mensaje")
        db.cerrar()
        self.id.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.stock.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.id.focus()

class WinModpro:
    def __init__(self, pkey):
        self.pkey= pkey
        self.modpro= tk.Tk()
        self.modpro.title("Modificar Productos")
        self.modpro.configure(background= "navy")
        fc.centrar(self.modpro,800,600)
        self.modpro.resizable(width=0, height=0)

        frame_titulo= tk.Frame(self.modpro, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Modificar Producto", font= ("Cheddar gothic",30), bg= "snow3", fg= "Black")
        etitulo.pack(side="top",fill= tk.X)
        frame_tree= tk.Frame(self.modpro, bd= 0, relief= tk.SOLID)
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
        frame_controles= tk.Frame(self.modpro, bd= 0, relief= tk.SOLID, bg= "black")
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

        self.modpro.mainloop()

    
    def dctabla(self, event):
        self.pri= str(self.tabla.item(self.tabla.selection())["values"][0])
        self.bmodificar["state"]= "normal"
        self.bborr["state"]= "normal"
        self.nombre.delete(0, tk.END)
        self.categoria.delete(0, tk.END)
        self.stock.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.nombre.insert(0, str(self.tabla.item(self.tabla.selection())["values"][1]))
        self.categoria.insert(0, str(self.tabla.item(self.tabla.selection())["values"][2]))
        self.stock.insert(0, str(self.tabla.item(self.tabla.selection())["values"][3]))
        self.precio.insert(0, str(self.tabla.item(self.tabla.selection())["values"][4]))

    def bmod(self):
        
        if fc.novacio(self.nombre.get()) and fc.novacio(self.categoria.get()) and fc.novacio(self.stock.get()) and fc.novacio(self.precio.get()): 
            self.db.consulta(f"""UPDATE almacen SET nombre="{self.nombre.get()}", categoria="{self.categoria.get()}", cantidad="{self.stock.get()}", precio="{self.precio.get()}" WHERE id="{self.pri}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Producto Modificado")
            self.nombre.delete(0, tk.END)
            self.categoria.delete(0, tk.END)
            self.stock.delete(0, tk.END)
            self.precio.delete(0, tk.END)
            self.db.mostrartree(self.tabla, """SELECT "id", "nombre", "categoria", "cantidad", "precio" FROM "almacen" """)
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"
        else:
            messagebox.showerror(message= "No se pueden ingresar campos vacios", title= "Error")
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"

    def bborrar(self):
        if messagebox.askyesno(message= "Confirma Borrar", title= "Borrar"):
            self.db.consulta(f"""DELETE FROM  almacen WHERE id="{self.pri}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Producto Borrado")
            self.nombre.delete(0, tk.END)
            self.categoria.delete(0, tk.END)
            self.stock.delete(0, tk.END)
            self.precio.delete(0, tk.END)
            self.db.mostrartree(self.tabla, """SELECT "id", "nombre", "categoria", "cantidad", "precio" FROM "almacen" """)
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"
    
    def bvol(self):
        self.db.cerrar()
        self.modpro.destroy()
        WinPersonal()

class WinListaClientes:
    def __init__(self, pkey):
        self.pkey= pkey
        self.listacli= tk.Tk()
        self.listacli.title("Clientes")
        self.listacli.configure(background= "navy")
        fc.centrar(self.listacli,800,600)
        self.listacli.resizable(width=0, height=0)

        frame_titulo= tk.Frame(self.listacli, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= "Lista Clientes", font= ("Cheddar gothic",30), bg= "snow3", fg= "Black")
        etitulo.pack(side="top",fill= tk.X)
        frame_tree= tk.Frame(self.listacli, bd= 0, relief= tk.SOLID)
        frame_tree.pack(expand= tk.YES, fill= tk.BOTH, padx=50, pady=15)
        self.tabla= Treeview(frame_tree, columns= ("#1","#2", "#3", "#4", "#5", "#6" ),height= 11, padding= 12 )
        self.tabla.grid(row= 2, column= 0, columnspan= 4)
        self.tabla.bind("<Double-Button-1>",self.dctabla)
        self.tabla["show"]= "headings"
        self.tabla.heading("#1", text= "ID", anchor= tk.CENTER)
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
        frame_controles= tk.Frame(self.listacli, bd= 0, relief= tk.SOLID, bg= "black")
        frame_controles.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)

        enombre= tk.Label(frame_controles, text= "Nombre Cliente", font= ("Times", 18), bg= "black", fg= "white")
        enombre.grid(row=0, column= 0,padx= 30 )
        self.nombre= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.nombre.grid(row= 0, column= 1, pady= 15, padx=50)
        eapellido= tk.Label(frame_controles, text= "Apellido", font= ("Times", 18), bg= "black", fg= "white")
        eapellido.grid(row= 1, column= 0)
        self.apellido= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.apellido.grid(row= 1, column= 1)
        email= tk.Label(frame_controles, text= "E-Mail", font= ("Times", 18), bg= "black", fg= "white")
        email.grid(row= 2, column= 0)
        self.mail= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.mail.grid(row= 2, column= 1, pady= 15)
        edireccion= tk.Label(frame_controles, text= "Direccion", font= ("Times", 18), bg= "black", fg= "white")
        edireccion.grid(row= 3, column= 0)
        self.direccion= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.direccion.grid(row= 3, column= 1)

        self.bmodificar= tk.Button(frame_controles, command= self.bmod, text= "Modificar", font= ("Times", 15),bg= "yellow", bd= 5)
        self.bmodificar.grid(row= 0, column= 2, padx= 20)    
        self.bmodificar["state"]= "disable"    
        self.bborr= tk.Button(frame_controles, command= self.bborrar, text= "Borrar", font= ("Times", 15), bg= "red", bd= 5)
        self.bborr.grid(row= 1, column= 2)
        self.bborr["state"]= "disable"
        self.bcarro= tk.Button(frame_controles, command= self.bborrar, text= "Carro", font= ("Times", 15), bg= "navy", fg= "white", bd= 5)
        self.bcarro.grid(row= 2, column= 2)
        self.bcarro["state"]= "disable"
        bvolver= tk.Button(frame_controles, command= self.bvol, text= "Volver", font= ("Times", 15), bg= "dim gray", bd= 5)
        bvolver.grid(row= 3, column= 2)

        self.db= fc.conexion("supermark.db")
        self.db.mostrartree(self.tabla, """SELECT "id", "nombre", "apellido", "mail", "direccion", "pedido" FROM "cliente" """)

        self.listacli.mainloop()

    def dctabla(self, event):
        self.pri= str(self.tabla.item(self.tabla.selection())["values"][0])
        if str(self.tabla.item(self.tabla.selection())["values"][5]) == "si":
            self.bcarro["state"]= "normal"
        else:
            self.bcarro["state"]= "disable"
        self.bmodificar["state"]= "normal"
        self.bborr["state"]= "normal"
        self.nombre.delete(0, tk.END)
        self.apellido.delete(0, tk.END)
        self.mail.delete(0, tk.END)
        self.direccion.delete(0, tk.END)
        self.nombre.insert(0, str(self.tabla.item(self.tabla.selection())["values"][1]))
        self.apellido.insert(0, str(self.tabla.item(self.tabla.selection())["values"][2]))
        self.mail.insert(0, str(self.tabla.item(self.tabla.selection())["values"][3]))
        self.direccion.insert(0, str(self.tabla.item(self.tabla.selection())["values"][4]))
        

    def bmod(self): 
        
        if fc.novacio(self.nombre.get()) and fc.novacio(self.apellido.get()) and fc.novacio(self.mail.get()) and fc.novacio(self.direccion.get()): 
            self.db.consulta(f"""UPDATE cliente SET nombre="{self.nombre.get()}", apellido="{self.apellido.get()}", mail="{self.mail.get()}", direccion="{self.direccion.get()}" WHERE id="{self.pri}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Cliente Modificado")
            self.nombre.delete(0, tk.END)
            self.apellido.delete(0, tk.END)
            self.mail.delete(0, tk.END)
            self.direccion.delete(0, tk.END)
            self.db.mostrartree(self.tabla, """SELECT "id", "nombre", "apellido", "mail", "direccion", "pedido" FROM "cliente" """)
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"
        else:
            messagebox.showerror(message= "No se pueden ingresar campos vacios", title= "Error")
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"

    def bborrar(self):
        if messagebox.askyesno(message= "Confirma Borrar", title= "Borrar"):
            self.db.consulta(f"""DELETE FROM  cliente WHERE id="{self.pri}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Producto Borrado")
            self.nombre.delete(0, tk.END)
            self.apellido.delete(0, tk.END)
            self.mail.delete(0, tk.END)
            self.direccion.delete(0, tk.END)
            self.db.mostrartree(self.tabla, """SELECT "id", "nombre", "apellido", "mail", "direccion", "pedido" FROM "cliente" """)
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"
    
    def bvol(self):
        self.db.cerrar()
        self.listacli.destroy()
        WinPersonal()    

class WinSecciones:
    def __init__(self, categoria):
        self.seccion= tk.Tk()
        self.seccion.title("Seccion")
        self.seccion.configure(background= "black")
        fc.centrar(self.seccion,800,600)
        self.seccion.resizable(width=0, height=0)

        frame_titulo= tk.Frame(self.seccion, bd= 0, relief= tk.SOLID)
        frame_titulo.pack(side= "top", expand= tk.NO, fill= tk.BOTH, padx=5, pady=5)
        etitulo= tk.Label(frame_titulo, text= f"{categoria}", font= ("Cheddar gothic",30), bg= "navy", fg= "red")
        etitulo.pack(side="top",fill= tk.X)
        frame_tree= tk.Frame(self.seccion, bd= 0, relief= tk.SOLID)
        frame_tree.pack(expand= tk.YES, fill= tk.BOTH, padx=50, pady=15)
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
        frame_controles= tk.Frame(self.seccion, bd= 0, relief= tk.SOLID, bg= "navy")
        frame_controles.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH, padx=5, pady=5)

        enombre= tk.Label(frame_controles, text= "Nombre Producto", font= ("Times", 18), bg= "navy", fg= "white")
        enombre.grid(row=0, column= 0,padx= 30 )
        self.nombre= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.nombre.grid(row= 0, column= 1, pady= 20, padx=50)
        ecantidad= tk.Label(frame_controles, text= "Cantidad", font= ("Times", 18), bg= "navy", fg= "white")
        ecantidad.grid(row= 2, column= 0)
        self.precio= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.precio.grid(row= 1, column= 1)
        eprecio= tk.Label(frame_controles, text= "Precio", font= ("Times", 18), bg= "navy", fg= "white")
        eprecio.grid(row= 1, column= 0)
        self.cantidad= tk.Spinbox(from_=0, to= 50, font= ("Times", 18), state= "readonly", command= self.total )
        self.cantidad.place(x=293, y=505, width= 305, height= 30)
        etotal= tk.Label(frame_controles, text= "Total", font= ("Times", 18), bg= "navy", fg= "white")
        etotal.grid(row= 3, column= 0)
        self.ttotal= tk.Entry(frame_controles, font= ("Times", 18), width= 25)
        self.ttotal.grid(row= 3, column= 1)

        self.agregar= tk.Button(frame_controles, text= "Agregar", font= ("Times", 15), bg= "green", bd= 5, fg= "white")
        self.agregar.grid(row= 1, column= 2)
        self.agregar["state"]= "disable"
        self.carro= tk.Button(frame_controles, text= "Carro", font= ("Times", 15), bg= "yellow", bd= 5)
        self.carro.grid(row= 2, column= 2, pady= 5)
        bvolver= tk.Button(frame_controles, command= self.bvol, text= "Volver", font= ("Times", 15), bg= "dim gray", bd= 5)
        bvolver.grid(row= 3, column= 2, pady= 5)

        self.db= fc.conexion("supermark.db")
        self.db.mostrartree(self.tabla, f"""SELECT "id", "nombre", "precio" FROM "almacen" WHERE categoria="{categoria}" and cantidad > 0""")

        self.seccion.mainloop()

    
    def dctabla(self, event):
        self.pri= str(self.tabla.item(self.tabla.selection())["values"][0])
        self.agregar["state"]= "normal"
        self.nombre["state"]= "normal"
        self.precio["state"]= "normal"
        self.nombre.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)
        self.ttotal.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.nombre.insert(0, str(self.tabla.item(self.tabla.selection())["values"][1]))
        self.precio.insert(0, str(self.tabla.item(self.tabla.selection())["values"][2]))
        self.nombre["state"]= "readonly"
        self.precio["state"]= "readonly"

    def total(self):
        self.ttotal["state"]= "normal"
        self.ttotal.delete(0, tk.END)
        self.ttotal.insert(0,str(int(self.cantidad.get()) * float(self.precio.get())))
        self.ttotal["state"]= "readonly"

    def bmod(self):
        
        if fc.novacio(self.nombre.get()) and fc.novacio(self.categoria.get()) and fc.novacio(self.stock.get()) and fc.novacio(self.precio.get()): 
            self.db.consulta(f"""UPDATE almacen SET nombre="{self.nombre.get()}", categoria="{self.categoria.get()}", cantidad="{self.stock.get()}", precio="{self.precio.get()}" WHERE id="{self.pri}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Producto Modificado")
            self.nombre.delete(0, tk.END)
            self.categoria.delete(0, tk.END)
            self.stock.delete(0, tk.END)
            self.precio.delete(0, tk.END)
            self.db.mostrartree(self.tabla, """SELECT "id", "nombre", "categoria", "cantidad", "precio" FROM "almacen" """)
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"
        else:
            messagebox.showerror(message= "No se pueden ingresar campos vacios", title= "Error")
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"

    def bborrar(self):
        if messagebox.askyesno(message= "Confirma Borrar", title= "Borrar"):
            self.db.consulta(f"""DELETE FROM  almacen WHERE id="{self.pri}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Producto Borrado")
            self.nombre.delete(0, tk.END)
            self.categoria.delete(0, tk.END)
            self.stock.delete(0, tk.END)
            self.precio.delete(0, tk.END)
            self.db.mostrartree(self.tabla, """SELECT "id", "nombre", "categoria", "cantidad", "precio" FROM "almacen" """)
            self.bmodificar["state"]= "disable"
            self.bborr["state"]= "disable"
    
    def bvol(self):
        self.db.cerrar()
        self.modpro.destroy()
        WinPersonal()

        
              
        
        
    


#WinPersonal()
#WinCliente()
#WinCarga("Admin01")        
#WinModpro("Admin01")
#WinListaClientes("Admin01")
#WinSecciones("Bebidas")

        


        
     


