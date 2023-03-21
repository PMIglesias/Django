print("Calculadora de Máximo Común Divisor (MCD)")


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

print("El Máximo Común Divisor (MCD) es: ",maximo_comun_divisor(num1, num2))