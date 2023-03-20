"""
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
"""

def get_int():
    while True:
        try:
            nro = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("NÚMERO ENTERO Dije!!! Reintente")
    return nro

# Programa Principal
numero = get_int()
print(f"Ingresaste el Número : {numero}")
