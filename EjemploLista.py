from turtle import pos


class Libro:
    def __init__(self,nombre, edicon):
        self.Nombre = nombre
        self.Edicion = edicon

    def __str__(self):
        return f"""Nombre: {self.Nombre}
{self.Edicion}""" 

class PilaLibros: 
    def __init__(self):
        self.lista = []
    
    def addLibro(self, obj):
        self.lista.append(obj)
    
    def editElement(self, obj, pos):
        self.lista[pos] = obj
    
    def deleteLibro(self, pos):
        self.lista.remove(pos)
    
    def searchBook(self,name):
        pos = 0
        for i in self.lista: 
            if name == Libro.Nombre: 
                return i, pos
            pos += 1
