#Iterativa:

def get_int():
    while True:
        try:
            num = int(input('Ingrese un número entero: '))
            return num
        except ValueError:
            print('El valor ingresado no es un número entero válido. Inténtelo de nuevo.')


#Recursiva

def get_int():
    try:
        num = int(input('Ingrese un número entero: '))
        return num
    except ValueError:
        print('El valor ingresado no es un número entero válido. Inténtelo de nuevo.')
        return get_int()