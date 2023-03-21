def contar_palabras(cadena):
    palabras = cadena.split()

    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario

cadena = "Hola mundo Hola mundo Hola Hola"
resultado = contar_palabras(cadena)
print(resultado)
