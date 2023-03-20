"""
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
● mostrar(): Muestra los datos de la cuenta.
● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
"""

class Cuenta:
    
    def __init__(self,titular,cantidad):
        titular = input("Ingrese nombre titular INICIAL :")
        self.__titular = titular
        self.__cantidad = cantidad
        
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, nombre):
        nombre = input("Ingrese nuevo nombre titular :")
        while True:
            if nombre.isalpha():
                self.__titular = nombre
                break
            else:
                nombre = input("NOMBRE -Solo caracteres alfabeticos-: ")

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, importe):
        self.__cantidad = importe
        
    def mostrar(self):
        print(f"Titular de la Cuenta : {self.titular} cantidad = {self.cantidad}")
        
    def ingresar(self):
        while True:
            try:
                importe = float(input("Importe Ingreso -Solo digitos-: "))
                break
            except:
                print("IMPORTE - SOLO DIGITOS")
        if importe > 0:
            self.cantidad = self.cantidad + importe
            modifica_titular = input("Modifica Titular? Ingrese S/s = ")
            if modifica_titular == "S" or modifica_titular == "s":
                self.titular = modifica_titular
                
    def retirar(self):
        while True:
            try:
                importe = float(input("Importe Retiro -Solo digitos-: "))
                break
            except:
                print("IMPORTE - SOLO DIGITOS")
        if importe > 0:
            self.cantidad = self.cantidad - importe
            modifica_titular = input("Modifica Titular? Ingrese S/s = ")
            if modifica_titular == "S" or modifica_titular == "s":
                self.titular = modifica_titular
                    
# ------------------------------------------------------------
# PROGRAMA PRINCIPAL

# Instancio el objeto
cuenta1 = Cuenta(titular="",cantidad=0.0)
# Proceso Ingreso
cuenta1.ingresar()
# Proceso Retiro
cuenta1.retirar()
# Muestra los datos modificados
cuenta1.mostrar()
