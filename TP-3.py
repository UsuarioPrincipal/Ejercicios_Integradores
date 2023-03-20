"""
3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
"""
def contar_palabras(cadena):
    # diccionario vacío para almacenar las palabras y su frecuencia
    frecuencia_palabras = {}
    # se genera la lista de palabras
    palabras = cadena.split()
    # se almacenan la palabra en el diccionario o se incrementa su frecuencia
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    # se devuelve el diccionario con las palabras y su frecuencia
    return frecuencia_palabras


# Programa Principal
cadena = input("Ingrese un texto sin signos de puntuación: ")
frecuencia_palabras = contar_palabras(cadena)
print(frecuencia_palabras)
