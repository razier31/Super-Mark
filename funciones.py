import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import sqlite3
import datetime


def imagen(ruta, tamaño):
    return ImageTk.PhotoImage(Image.open(ruta).resize(tamaño, Image.ANTIALIAS))

def centrar(root, ancho, largo):
    pantancho= root.winfo_screenwidth()
    pantlargo= root.winfo_screenheight()
    x = int((pantancho/2)-(ancho/2))
    y = int((pantlargo/2)-(largo/2))
    return root.geometry(f"{ancho}x{largo}+{x}+{y}")

def novacio(dato):
    if len(dato)>0:
       return True
    else:
        return False

def fecha():
    tiempoactual= datetime.datetime.now()
    factual= datetime.datetime.strftime(tiempoactual, "%d/%m/%Y")
    return factual

def hora():
    tiempoactual= datetime.datetime.now()
    hactual= datetime.datetime.strftime(tiempoactual, "%H:%M")
    return hactual


class conexion():
    
    def __init__(self,bd):
        self.conexion = sqlite3.connect(bd)
        self.cursor = self.conexion.cursor()

    def consulta(self, consulta):
        self.cursor.execute(consulta)
    
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()

    def validar(self,consulta):
        self.cursor.execute(consulta)
        datos= self.cursor.fetchone()
        if datos != None:
            return True
        else:
            return False
        
    def contar(self,consulta):
        self.cursor.execute(consulta)
        cont= self.cursor.fetchone()
        return cont[0]
    
    def sumar(self,consulta):
        self.cursor.execute(consulta)
        sumar= self.cursor.fetchall()
        acu=0
        for numero in sumar:
            acu+= numero[0] 
        return acu

    def fall(self,consulta):
        self.cursor.execute(consulta)
        datos= self.cursor.fetchall()
        return datos


    def mostrartree(self, tree,consulta):
        self.cursor.execute(consulta)
        data= tree.get_children()
        for item in data:
            tree.delete(item)
        datos= self.cursor.fetchall()
        for dato in datos:
            tree.insert("",tk.END, values= dato)


fecha()



        



