class Persona:
    def __init__(self, nombre, apellido, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.ocupacion = ocupacion

    def imprimirnombrelargo(self):
        return f'El nombre Largo {self.nombre} {self.apellido}'


persona1 = Persona("Juan", "Perez", "Ingeniero")
persona2 = Persona("Maria" , "Gonzales" , "Contadora")

#print(persona1.imprimirnombrelargo)
#print(persona2.imprimirnombrelargo)


class Estudiante(Persona):
    def __init__(self, nombre, apellido, ano, ocupacion):
        Persona.__init__(self, nombre, apellido, ocupacion)
        self.graduacion = ano

    def bienvenida(self):
        super().imprimirnombrelargo()
        return f'Su ano de graduacion es {self.graduacion}'

Estudiante = Estudiante("Jose", "lal uz", 2022, "Programador")
#print(Estudiante1.apellido)

#Estudiante.bienvenida()

print(Estudiante1.bienvenida())

print(Estudiante1.imprimirnombrelargo())
