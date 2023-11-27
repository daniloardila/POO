class TanqueDeGas:
    def __init__(self):
        self.gas = 100
        
    def agregar_gas(self, cantidad):
        self.gas += cantidad
        
    def obtener_gas(self):
        return self.gas
    
    def usar_gas(self, cantidad):
        self.gas -= cantidad


class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_gas() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_gas(distancia / 2)
            print("Movido")
        else:   
            print("Echele")
            
    def obtener_posicion(self):
        return self.posicion
            

        
        
tanque = TanqueDeGas()
auto = Auto(tanque)

print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(20)
print(auto.obtener_posicion())
auto.mover(60)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())

    