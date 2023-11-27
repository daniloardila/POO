class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f'Estudiando: {self.nombre}')
        
nombre = input("Diga nombre: ")
edad = input("Diga edad: ")
grado = input("Diga grado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
    Nombre: {estudiante.nombre} \n 
    Edad: {estudiante.edad} \n 
    Grado: {estudiante.grado} \n   
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()