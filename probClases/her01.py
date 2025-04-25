from multimethod import multimethod

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    @multimethod
    def modificar(self, x:str):
        self.nombre = x
        
    @multimethod
    def modificar(self, x:int):
        self.edad  = x
        
    def __str__(self):
        return (f"{self.nombre, self.edad}")
    
class main():
    ob1 = Persona("hola", 23)
    print(ob1)
    ob1.modificar("richar")
    print(ob1)
    ob1.modificar(2)
    print(ob1)