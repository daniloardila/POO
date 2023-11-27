def decorador(funcion):
    def funcion_modificada():
        print("antes")
        funcion()
        print("despues")
    return funcion_modificada

# def saludo():
#     print("hola")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
     print("hola")
     
saludo()