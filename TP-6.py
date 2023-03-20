# ------------------------------------------------------------
# Problema 6:
"""
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
● mostrar(): Muestra los datos de la persona.
● es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad
"""

class Persona:

    def __init__(self,nombre,edad,dni):
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, name):
        while True:
            if name.isalpha():
                self.__nombre = name
                break
            else:
                name = input("NOMBRE -Solo caracteres alfabeticos-: ")
                
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, años):
        while True:
            if años.isdigit():
                self.__edad = int(años)
                break
            else:
                años = input("AÑOS -Solo digitos-: ")

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, documento):
        while True:
            if documento.isdigit():
                self.__dni = int(documento)
                break
            else:
                documento = input("DNI -Solo digitos-: ")
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"dni: {self.dni}")
    
    def es_mayor_de_edad(self):
        if self.edad > 17:
            return True
        else:
            return False
        
# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# Instancio el objeto
persona1 = Persona(nombre="",edad=0,dni=0)
# Ingreso los datos
persona1.nombre = input("Nombre de la persona = ")
persona1.edad = input("Edad de la persona = ")
persona1.dni = input("DNI = ")
# Muestro los datos
persona1.mostrar()
# Determino si es mayor de edad
if persona1.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("NO es mayor de edad")
    