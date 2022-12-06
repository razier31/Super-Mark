from Interfaz.ventanas import *
import tkinter as tk
from tkinter.ttk import *
import funciones as fc
from tkinter import messagebox
import datetime

class Main(WinMain):
    def __init__(self):
        super().__init__()
        

    def binicio(self):
        global pkey
        bd= fc.conexion("supermark.db")
        us= bd.validar(f"SELECT usuario FROM user WHERE usuario= '{self.usuario.get()}'")
        ps= bd.validar(f"SELECT pass FROM user WHERE pass= '{self.password.get()}' and usuario= '{self.usuario.get()}'")
        ad= bd.validar(f"SELECT admin FROM user WHERE admin= 'si' and usuario= '{self.usuario.get()}'")
        if  us  and ps:
            if ad :
                bd.cerrar()
                pkey = self.usuario.get()
                self.win.destroy()
                Personal()
            else:
                pkey = self.usuario.get()
                bd.consulta(f"""CREATE TABLE IF NOT EXISTS carro_{pkey} 
                (pos INTEGER PRIMARY KEY AUTOINCREMENT,
                id INTEGER NOT NULL,
                producto TEXT  NOT NULL,
                precio REAL NOT NULL,
                cantidad INTEGER NOT NULL,
                total REAL NOT NULL)""")
                bd.cerrar()
                self.win.destroy()
                Cliente()
        else:
            messagebox.showerror(message= "La contraseña o el usuario es Incorrecto", title= "Mensaje")

    def bregistro(self):
        self.win.destroy()
        Registro()

class Registro(WinRegistro):
        def __init__(self):
            super().__init__()

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
                self.win.destroy()
                Main()

            except:
                messagebox.showerror(message= "El nombre de usuario ya Existe", title= "Mensaje")
            db.cerrar()

    
        def bvolver(self):
            self.win.destroy()
            Main()

class Cliente(WinCliente):
    def __init__(self):
        super().__init__()

    def bot1(self):        
        self.win.destroy()
        Secciones("Bebidas")

    def bot2(self):        
        self.win.destroy()
        Secciones("Congelados")

    def bot3(self):        
        self.win.destroy()
        Secciones("Cuidado Personal")

    def bot4(self):        
        self.win.destroy()
        Secciones("Despensa")

    def bot5(self):        
        self.win.destroy()
        Secciones("Limpieza")

    def bot6(self):        
        self.win.destroy()
        Secciones("Refrigerados")

    def bcarro(self):
        self.win.destroy()
        Carro()

    def bsalir(self):
        self.win.destroy()
        Main()
            
class Personal(WinPersonal):
    def __init__(self):
        super().__init__()
        
    
    def btcar(self):
        self.win.destroy()
        Carga()

    def btmodi(self):
        self.win.destroy()
        Modpro()

    def btlistar(self):
        self.win.destroy()
        ListaClientes()

    def btsalir(self):
        self.win.destroy()
        Main()

class Carga(WinCarga):
    def __init__(self):
        super().__init__()
        

    def bvolver(self):
        self.win.destroy()
        Personal()

    def bguardar(self):
        db= fc.conexion("supermark.db")
        try:
            db.consulta(f"""INSERT INTO almacen VALUES("{self.id.get()}","{self.nombre.get()}","{self.categoria.get()}","{self.stock.get()}","{self.precio.get()}","{pkey}")""")
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

class Modpro(WinModpro):
    def __init__(self):
        super().__init__()
        
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
            self.db.consulta(f"""UPDATE almacen SET nombre="{self.nombre.get()}", categoria="{self.categoria.get()}", cantidad= "{self.stock.get()}", precio="{self.precio.get()}" WHERE id="{self.pri}" """)
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
        self.win.destroy()
        Personal()

class ListaClientes(WinListaClientes):
    def __init__(self):
        super().__init__()

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
            self.db.consulta(f"""UPDATE cliente SET nombre="{self.nombre.get()}", apellido="{self.apellido.get()}", mail="{self.mail.get()}", direccion="{self.direccion.get()}" WHERE usuario="{self.pri}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Cliente Modificado")
            self.nombre.delete(0, tk.END)
            self.apellido.delete(0, tk.END)
            self.mail.delete(0, tk.END)
            self.direccion.delete(0, tk.END)
            self.db.mostrartree(self.tabla, """SELECT "usuario", "nombre", "apellido", "mail", "direccion", "pedido" FROM "cliente" """)
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

    def btcarro(self):
        user= self.pri
        self.win.destroy()
        CarroAdmin(user)

    def bfpedido(self):
        self.win.destroy()
        ListaPedidos()
        
    
    def bvol(self):
        self.db.cerrar()
        self.win.destroy()
        Personal()    

class Secciones(WinSecciones):
    def __init__(self, categoria):
        super().__init__(categoria)
    
    def dctabla(self, event):
        self.pri= str(self.tabla.item(self.tabla.selection())["values"][0])
        self.bagregar["state"]= "normal"
        self.nombre["state"]= "normal"
        self.precio["state"]= "normal"
        self.total["state"]= "normal"
        self.nombre.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)
        self.total.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.nombre.insert(0, str(self.tabla.item(self.tabla.selection())["values"][1]))
        self.precio.insert(0, float(self.tabla.item(self.tabla.selection())["values"][2]))
        self.nombre["state"]= "readonly"
        self.precio["state"]= "readonly"
        self.total["state"]= "readonly"


    def ftotal(self):
        self.total["state"]= "normal"
        self.total.delete(0, tk.END)
        self.total.insert(0,float(int(self.cantidad.get()) * float(self.precio.get())))
        self.total["state"]= "readonly"

    def bfagregar(self):
        self.nombre["state"]= "normal"
        self.precio["state"]= "normal"
        self.cantidad["state"]= "normal"
        self.total["state"]= "normal"
        pedido = self.db.validar(f"SELECT pedido FROM cliente WHERE usuario= '{pkey}' and pedido='no' ")
        if (self.db.contar(f"""SELECT COUNT(producto) FROM carro_{pkey}  """)) < 30 and pedido:
            if fc.novacio(self.nombre.get()) and fc.novacio(self.precio.get()) and fc.novacio(self.cantidad.get()) and fc.novacio(self.total.get()):
                self.db.consulta(f"""INSERT INTO carro_{pkey} VALUES(null, {self.pri}, "{self.nombre.get()}","{self.precio.get()}","{self.cantidad.get()}","{self.total.get()}")""")
                self.db.commit()
                self.nombre.delete(0, tk.END)
                self.cantidad.delete(0, tk.END)
                self.total.delete(0, tk.END)
                self.precio.delete(0, tk.END)
                self.nombre["state"]= "readonly"
                self.precio["state"]= "readonly"
                self.cantidad["state"]= "readonly"
                self.total["state"]= "readonly"
                messagebox.showinfo(title= "Informacion", message="Producto Agregado al Carro")
            else:
                messagebox.showinfo(title= "Informacion", message="Existen campos Vacios Por Favor seleccione el producto y despues la Cantidad")
        else:
            messagebox.showerror(title= "Carro", message= "Carro lleno o Pedido Realizado")
        if pedido:
            carro= (self.db.contar(f"""SELECT COUNT(producto) FROM carro_{pkey}  """)) 
            self.info["text"]= f"Info: El carro tiene {carro} productos de 30"
        else:
            self.info["text"]= f"Info: Pedido Realizado"

        
    def bfcarro(self):
        self.win.destroy()
        Carro()
            
    def bfvol(self):
        self.db.cerrar()
        self.win.destroy()
        Cliente()

class Carro(WinCarro):
    def __init__(self):
        super().__init__()

    def mostrar(self):
        self.db.mostrartree(self.tabla, f"""SELECT "pos", "producto", "precio", "cantidad", "total" FROM carro_{pkey}  """)
        pedido = self.db.validar(f"SELECT pedido FROM cliente WHERE usuario= '{pkey}' and pedido='no' ")
        if pedido:
            self.bfinalizar["state"]= "normal"
            self.bcancelar["state"]= "disable"
        else:
            self.bfinalizar["state"]= "disable"
            self.bcancelar["state"]= "normal"

    def dctabla(self, event):
        self.pri= str(self.tabla.item(self.tabla.selection())["values"][0])
        pedido = self.db.validar(f"SELECT pedido FROM cliente WHERE usuario= '{pkey}' and pedido='no' ")
        if pedido:
            self.bquitar["state"]= "normal"
        else:
            self.bquitar["state"]= "disable"
        

    def ftotal(self):
        self.total["state"]= "normal"
        self.total.delete(0, tk.END)
        self.total.insert(0, "$"+str(self.db.sumar(f"""SELECT "total" FROM carro_{pkey}  """)))
        self.total["state"]= "readonly"

    def bffinalizar(self):
        self.db.consulta(f"""UPDATE cliente SET pedido="si" WHERE usuario="{pkey}" """)
        self.db.consulta(f"""INSERT INTO pedido VALUES( null,"{fc.fecha()}","{fc.hora()}","{pkey}", null, null, null)""")
        self.db.commit()
        messagebox.showinfo(title= "Informacion", message="Pedido Realizado")
        self.bfinalizar["state"]= "disable"
        self.bcancelar["state"]= "normal"

    def bfcancelar(self):
        if messagebox.askyesno(message= "Confirma Cancelar el Pedido", title= "Cancelar"):
            self.db.consulta(f"""UPDATE cliente SET pedido="no" WHERE usuario="{pkey}" """)
            self.db.consulta(f"""DELETE FROM  pedido WHERE usuario="{pkey}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Pedido Cancelado")
            self.bfinalizar["state"]= "normal"
            self.bcancelar["state"]= "disable"

    def bfquitar(self):
        if messagebox.askyesno(message= "Confirma Borrar", title= "Borrar"):
            self.db.consulta(f"""DELETE FROM  carro_{pkey} WHERE pos="{self.pri}" """)
            self.db.commit()
            messagebox.showinfo(title= "Informacion", message="Producto Borrado")
            self.bquitar["state"]= "disable"
            self.mostrar()
            self.ftotal()

    def bfvolver(self):
        self.win.destroy()
        Cliente()

class CarroAdmin(WinCarroAdmin):
    def __init__(self, user):
        super().__init__(user)
        self.user= user
    
    def mostrar(self):
        self.db.mostrartree(self.tabla, f"""SELECT "pos", "producto", "precio", "cantidad", "total" FROM carro_{self.user}  """)
        
    
    def ftotal(self):
        self.total["state"]= "normal"
        self.total.delete(0, tk.END)
        self.total.insert(0, "$"+str(self.db.sumar(f"""SELECT "total" FROM carro_{self.user}  """)))
        self.total["state"]= "readonly"

    def bfenviar(self):
        if messagebox.askyesno(message= "Confirma Realizar el Envio", title= "Envio"):
            self.db.consulta(f"""UPDATE cliente SET pedido="no" WHERE usuario="{self.user}" """)
            total= self.db.sumar(f"""SELECT "total" FROM carro_{self.user}  """)
            self.db.consulta(f"""UPDATE pedido SET total= "{total}", f_entrega= "{fc.fecha()}", h_entrega= "{fc.hora()}" WHERE usuario="{self.user}" """)
            datos= self.db.fall(f"""SELECT "id", "cantidad" FROM carro_{self.user}  """)
            self.db.consulta(f"""DROP TABLE carro_{self.user} """)
            messagebox.showinfo(title= "Informacion", message="Pedido Enviado")
            for id, vendido in datos:
                self.db.consulta(f"""UPDATE almacen SET cantidad= cantidad-"{vendido}" WHERE id="{id}" """)
            messagebox.showinfo(title= "Informacion", message="El stock del Almacen a sido Actualizado")    
            self.db.commit()

    def bfvolver(self):
        self.win.destroy()
        ListaClientes()
                       
class ListaPedidos(WinListaPedidos):
    def __init__(self):
        super().__init__()

    def mostrar(self):
        self.db.mostrartree(self.tabla, f"""SELECT "id", "f_pedido", "h_pedido", "usuario", "total", "f_entrega", "h_entrega" FROM pedido  """)    

    def bfvolver(self):
        self.win.destroy()
        ListaClientes()

    

