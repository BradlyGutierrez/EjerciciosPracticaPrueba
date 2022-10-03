class Libro:
    def __init__(self,nombre, edicon):
        self.Nombre = nombre
        self.Edicion = edicon

    def __str__(self):
        return f"""Nombre: {self.Nombre}
{self.Edicion}""" 

class PilaLibros: 
    def __init__(self):
        self.pila = []
    
    def apilarLibro(self, obj):
        self.pila.append(obj)
    
    def sacarLibro(self):
        self.pila.pop()
    
    def mostrarPila(self):
        cima = len(self.pila)-1
        while cima >= 0:
            print(self.pila[cima])
            cima -= 1
        print("="*50)

pilaDeLibro = PilaLibros()

def apilar():
    nombre = input("Nombre: ")
    edicion = input("Edición: ")
    lbt = Libro(nombre, edicion)
    pilaDeLibro.apilarLibro(lbt)


pilaDeLibro.mostrarPila()