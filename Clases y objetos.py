class Celular():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def llamar(self):
        print(f'llamando desde: {self.modelo}')
        
celular1 = Celular("Samsung","S23")
celular2 = Celular("Apple","Iphone 15")
celular2.llamar()