class Auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "enecendido"
        print("encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("conduciendo")
        
auto = Auto()
auto.conducir()
        