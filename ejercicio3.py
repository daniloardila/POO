class Personaje():
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __str__(self):
        return f"{self.nombre},(fuerza {self.fuerza}, velocidad {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2)**2
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje("goku",100, 100)
vegeta = Personaje("vegeta",99, 99)

gogeta = goku + vegeta

print(gogeta)