import sqlite3

conexion = sqlite3.connect("supermark.db")
cursor = conexion.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS cliente
(id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre CHAR(30)  NOT NULL,
apellido CHAR(30) NOT NULL,
mail CHAR(30) NOT NULL,
direccion CHAR(30) NOT NULL,
usuario CHAR(20), 
FOREIGN KEY(usuario) REFERENCES user(usuario))""") 

#prueba= ["SuperMark","Admin"]

#cursor.execute("""INSERT INTO user VALUES
#(?,?)""", prueba)

#conexion.commit()

conexion.close()

print("Base de Datos Creada")