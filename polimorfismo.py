class Gato():
    def sonido(self):
        return "miau"

class Perro():
    def sonido(self):
        return "guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

print(gato.sonido())

hacer_sonido(gato)