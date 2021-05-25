#Metodo constructor
class Persona:
    pass
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre,self.año)
    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre,frase)

persona = Persona('Camilo',25)
print(persona.descripcion())
print(persona.comentario('hola que tal?'))


#Modificar un atributo
class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

myCorreo = Email()
print(myCorreo.enviado)
myCorreo.enviar_correo()
print(myCorreo.enviado)