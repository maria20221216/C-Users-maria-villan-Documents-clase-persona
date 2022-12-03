class Persona:
    def __init__(self,nombre,fecha,dni,cuenta):
        self.nombre = nombre
        self.fecha = fecha
        self.dni= dni
        self.cuenta= cuenta
         
    def saludo(self):
       print("hola")
    
persona = Persona("paula monti", "12-12-1906","111876","456789")
persona2 = Persona("sofia paredes","12/12/1990","30111222","905644")

print (persona.nombre,persona.fecha, persona.dni, persona.cuenta)

print(persona2.nombre, persona2.fecha, persona2.dni, persona2.cuenta)




