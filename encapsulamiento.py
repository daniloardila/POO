class MiClase:
     def __init__(self):
         self._atributo_privado = "valor"
         
objeto = MiClase()
print(objeto._atributo_privado)

class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
        
dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre)
       
