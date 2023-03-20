"""
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
● Un constructor.
● Los setters y getters para el nuevo atributo.
● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
● Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta
"""
# del ejercicio 7

class Cuenta:
    
    def __init__(self,titular,cantidad):
        titular = input("Ingrese nombre titular INICIAL : ")
        self.__titular = titular
        self.__cantidad = cantidad
        
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, nombre):
#        nombre = input("Ingrese nuevo nombre titular :")
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
            modifica_titular = input("Modifica Titular? Ingrese Nuevo Nombre / Enter=NO: ")
            if modifica_titular != "":
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
            modifica_titular = input("Modifica Titular? Ingrese Nuevo Nombre / Enter=NO: ")
            if modifica_titular != "":
                self.titular = modifica_titular
                    


class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad, edad, bonificacion):
        Cuenta.__init__(self, titular, cantidad)
        while True:
            try:
                edad = int(input("Cta. Joven - Ingrese edad : "))
                break
            except:
                print("EDAD - SOLO DIGITOS")
        if edad > 17 and edad < 25:
            self.__edad = int(edad)
        else:
            self.__edad = 0
        while True:
            try:
                bonificacion = input("Cta. Joven - Ingrese bonificacion hasta 100%: ")
                if float(bonificacion) <= 100:
                    self.__bonificacion = float(bonificacion)
                else:
                    self.__bonificacion = 100
                break
            except:
                print("BONIFICACION - SOLO DIGITOS")
                            
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, importe):
        self.__bonificacion = importe

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, años):
        self.__edad = años
        
    def es_titular_valido(self):
        if self.edad > 17 and self.edad < 25:
            return True
        else:
            return False
        
    def mostrar(self):
        print(f"CUENTA JOVEN - Bonificación = {self.bonificacion}% / Titular de la Cuenta : {self.titular} / cantidad = {self.cantidad}")

    def retirar(self):
        if not(cuenta1.es_titular_valido()):
            print("RETIRO DENEGADA - CTA. JOVEN EDAD -Solo mayores 17 y menores 25-")
        else: # ejecuto operaciones
            while True:
                try:
                    importe = float(input("Importe Retiro JOVEN -Solo digitos-: "))
                    break
                except:
                    print("IMPORTE - SOLO DIGITOS")
            if importe > 0:
                self.cantidad = self.cantidad - importe
                modifica_titular = input("Modifica Titular? Ingrese Nuevo Nombre / Enter=NO: ")
                if modifica_titular != "":
                    self.titular = modifica_titular
# ------------------------------------------------------------
# PROGRAMA PRINCIPAL

# Apertura de cuenta
tipo_cuenta=input("Desea abrir cuenta Joven Ingrese S/s: ")
if tipo_cuenta == "S" or tipo_cuenta == "s": # Instancio el objeto Cta Joven
    cuenta1 = CuentaJoven(titular="", cantidad=0.0, edad=0, bonificacion=0.0,)
    if not(cuenta1.es_titular_valido()):
        del(cuenta1)
        print("APERTURA DENEGADA - CTA. JOVEN EDAD -Solo mayores 17 y menores 25-")
    else:
        # Ejecuto Operaciones
        cuenta1.ingresar()
        cuenta1.retirar()
        cuenta1.mostrar()
else: # Instancio el objeto Cta Normal
    cuenta1 = Cuenta(titular="",cantidad=0.0)
    # Ejecuto Operaciones
    cuenta1.ingresar()
    cuenta1.retirar()
    cuenta1.mostrar()

