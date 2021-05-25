#Herencia

class pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre,self.tipo)

class pikachu(pokemon):
    def ataque(self, tipoAtaque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoAtaque)

class charmander(pokemon):
    def ataque(self, tipoAtaque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoAtaque)

nuevo_pokemon = pikachu('Boby','Trueno')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('Impactrueno'))