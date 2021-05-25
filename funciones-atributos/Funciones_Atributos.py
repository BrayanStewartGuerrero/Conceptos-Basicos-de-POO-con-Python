class Persona:
    edad = 27
    nombre = 'Victor'
    pais = 'Colombia'

doctor = Persona()
print('El nombre es:',doctor.nombre)
print('La edad es:',getattr(doctor, 'edad'))

#Retorna true/false si existe o no ese atributo
print('El doctor tiene una edad?',hasattr(doctor,'edad'))

#Cambio el valor del atributo en el objeto
setattr(doctor,'nombre','Hector')
print(doctor.nombre)

##Elimino el atributo de la clase
delattr(Persona,'pais')