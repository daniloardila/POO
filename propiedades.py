class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property    
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre
        
dalto = Persona("Lucas", 21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "pepe"

nombre = dalto.nombre
print(nombre)