class Usuario:
    def __init__(self, user, pasw, nombre, apellido):
        self.__user= user
        self.__pasw= pasw
        self.__nombre= nombre
        self.__apellido= apellido

    def get_user(self):
        return self.__user
    def set_user(self, user):
        self.__user= user

    def get_pasw(self):
        return self.__pasw
    def set_pasw(self, pasw):
        self.__pasw= pasw    

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre= nombre  

    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido= apellido  

class Cliente(Usuario):
    def __init__(self, user, pasw, nombre, apellido, mail, direccion):
        super().__init__(user, pasw, nombre, apellido)
        self.__mail= mail
        self.__direccion= direccion

    def get_mail(self):
        return self.__mail
    def set_apellido(self, mail):
        self.__mail= mail  

    def get_direccion(self):
        return self.__direccion
    def set_direccion(self, direccion):
        self.__direccion= direccion

class Personal(Usuario):
    def __init__(self, user, pasw, nombre, apellido, cargo, dni):
        super().__init__(user, pasw, nombre, apellido)
        self.__cargo= cargo  
        self.__dni= dni

    def get_cargo(self):
        return self.__cargo
    def set_cargo(self, cargo):
        self.__cargo= cargo  

    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni= dni

class Producto:
    def __init__(self, id, nombre, categoria, stock, precio):
        self.__id= id
        self.__nombre= nombre
        self.__categoria= categoria
        self.__stock= stock
        self.__precio= precio

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id= id

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre= nombre

    def get_categoria(self):
        return self.__categoria
    def set_categoria(self, categoria):
        self.__categoria= categoria

    def get_stock(self):
        return self.__stock
    def set_stock(self, stock):
        self.__stock= stock

    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio= precio
        

class Carrito:
    def __init__(self,cliente, listapro):
        self.cliente= cliente
        self.listapro= listapro