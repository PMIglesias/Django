def contar_palabras():
    cadena = input('Ingrese una cadena de caracteres: ')
    palabras = cadena.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    max_frecuencia = 0
    max_palabra = ''
    for palabra, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            max_palabra = palabra
    return (max_palabra, max_frecuencia)