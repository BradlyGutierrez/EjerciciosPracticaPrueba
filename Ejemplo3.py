import statistics
class Paciente: 
    def __init__(self,nombre,edad,fecha,dom):
        self.Nombre = nombre
        self.Edad = edad
        self.Fecha = fecha
        self.Domicilio = dom

    def __str__(self):
        return f"""Nombre: {self.Nombre}
Edad: {self.Edad}
fecha de ingreso: {self.Fecha}
Domicilio: {self.Domicilio}
"""
class ColaDePacientes: 
    def __init__(self):
        self.lista = []
    
    def agregarPaciente(self, obj):
        self.lista.append(obj)
    

lst = ColaDePacientes()

def menu():
    print("Lista")
    print("1. Ingresar")
    print("2. Mostrar")
    print("3. Mostrar")

def agregarPac():
    name = input("Name: ")
    age = float(input("Edad: "))
    date = input("Fecha de ingreso en formato d/m/y: ")
    dom = input("Domicilio: ")
    pac = Paciente(name,age,date,dom)
    lst.agregarPaciente(pac)

def moda():
    suma = 0
    contador = 0
    for i in lst.lista:
        if i.Edad > 20 and i.Edad<30:
            contador = contador +1
            suma = suma + i.Edad
    media = suma / contador
    return media

def imprimirPacEdad():
    try:
        for i in lst.lista:
            if i.Edad > 20 and i.Edad<30:
                print(i)
                print(moda())
                
    except Exception as ex:
        print(str(ex))


def recursividad(final):
   
    if lst.lista[final] == lst.lista[0]:
        print(lst.lista[final].Edad)
    else:
        print(lst.lista[final].Edad)
        recursividad(final - 1)
        
final = len(lst.lista)-1
def principal():
    
    op = 0
    while (op != 3):
        menu()
        op = int(input())
        if (op == 1):
            agregarPac()
        elif (op == 2):
            imprimirPacEdad()
        elif (op == 3):
                recursividad(final)

principal()