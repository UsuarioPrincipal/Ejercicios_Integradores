"""
4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
"""



# Funcion del TP 3

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

def palabra_mas_repetida(frecuencia_palabras):
    # Encuentra la palabra más repetida y su frecuencia
    palabra = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frec = frecuencia_palabras[palabra]

    # Devuelve la tupla con la palabra más repetida y su frecuencia
    return (palabra, frec)


# Programa Principal

cadena = input("Ingrese un texto sin signos de puntuación: ")
frecuencia = contar_palabras(cadena)
palabra, frec = palabra_mas_repetida(frecuencia)
print(f"La palabra mas repetida es: {palabra} y se repite {frec} veces")




