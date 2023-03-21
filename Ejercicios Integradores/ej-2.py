print("Calculadora de Mínimo común múltiplo (MCM)")


print("Ingrese el primer número: ")
num1=input()
print("ingrese el 2do número: ")
num2=input()

def maximo_comun_divisor(num1, num2):
    temporal = 0
    while num2 != 0:
        temporal = num2
        num2 = int(num1) % int(num2)
        num1 = temporal
    return num1

def minimo_comun_multiplo(num1, num2):
    return (int(num1)  * int(num2) ) / maximo_comun_divisor(num1, num2)



print("El Mínimo común múltiplo (MCM) es: ",minimo_comun_multiplo(num1, num2))