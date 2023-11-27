from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"nombre: {self.nombre} tengo {self.edad} años")


# dalto.trabajar()    

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Trabajo en: {self.actividad}")
        
        
dalto = Estudiante("lucas",21,"Masculino","programacion")

fabian = Trabajador("fabian",45,"Masculino","programacion")

dalto.presentarse()
dalto.hacer_actividad()

fabian.presentarse()
fabian.hacer_actividad()
