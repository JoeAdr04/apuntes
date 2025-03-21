class Fraccion:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador  = denominador
    
    def __str__(self):
        return (f"{self.__numerador}/{self.__denominador}")
    
    def __add__(self, otro):
        valor = otro
        return Fraccion(self.__numerador+valor, self.__denominador)
    
    def __mul__(self, otro):
        if isinstance(otro, Fraccion):
            numerador = self.__numerador * otro.__numerador
            denominador = self.__denominador * otro.__denominador
            return Fraccion(numerador, denominador)
        
        elif isinstance(otro, int):
            numerador = self.__numerador*otro
            return Fraccion(numerador, self.__denominador)
        
        else:
            print("no hace nada")
            
    def simplificar(self):
        primos = ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
        for i in range(0, len(primos)):
            divNum = self.__numerador/primos[i]
            divDen = self.__denominador/primos[i]
            if (divNum%1 == 0 and divDen%1 == 0):
                self.__numerador = divNum
                self.__denominador = divDen
                
                break
            
            
class main():
    fraccion1 = Fraccion(9,6)
    fraccion2 = Fraccion(25,5)
    print(fraccion1)
    fraccion1.simplificar()
    
    print(fraccion1)
    print(fraccion2)
    
    fraccion2.simplificar()
    print(fraccion2)
    #nuevo = 5
    #suma = fraccion1 + nuevo
    #adicional = suma + nuevo
    #print(suma)
    #print(adicional)
    #nuevoNum = 3
    #mult1 = fraccion1 * nuevoNum
    #mult2 = fraccion1 * fraccion2
    #print(mult1)
    #print(mult2)