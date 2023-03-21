class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad