#Metodos
class Matematicas:
    def suma(self):
        self.n1 = 2
        self.n2 = 3

s = Matematicas()
s.suma()
print(s.n1 + s.n2)

class Ropa:
    def __init__(self):
        self.marca = 'adidas'
        self.talla = 'XL'
        self.color = 'negro'

camisa = Ropa()
print(camisa.marca)
print(camisa.talla)
print(camisa.color)

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 + n2
        self.division = n1 / n2

operacion = Calculadora(2,3)
print(operacion.suma)