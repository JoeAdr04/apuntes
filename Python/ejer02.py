class Empleado:
    def __init__(self,nombre,sueldo):
        self.__nombre = nombre
        self.sueldo = sueldo
    def __str__(self):
        return f'Nombre: {self.__nombre} Salario: {self.sueldo}'
    
    def sueldoAnual(self):
        sueldoAnual = self.sueldo*12
        return sueldoAnual
    def aumento(self):
        self.sueldo = self.sueldo*(1.10)
    def getNombre(self):
        return self.__nombre
        
class main():
    emp01 = Empleado("jose", 1800.50)
    emp02 = Empleado("pedrito", 7826.50)
    print("Empleado 1:")
    print(emp01)
    print("Empleado 2:")
    print(emp02)
    print(f'Sueldo anual empelao 1:{emp01.sueldoAnual()}')
    print(f'Sueldo anual empelao 2:{emp02.sueldoAnual()}')
    emp01.aumento()
    emp02.aumento()
    print("empleado 1 despues del aumento")
    print(emp01)
    print("empleado 2 despues del aumento")
    print(emp02)
    print(emp01.getNombre())