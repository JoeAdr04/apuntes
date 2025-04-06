class AlgebraVectorial:
    def __init__(self):
        self.__a = []
        self.__b = []
    
    def agregarA(self,a):
        self.__a.append(a)
    def agregarB(self,a):
        self.__b.append(a)
    
    def mostrar(self):
        cad = ""
        for i in range(len(self.__a)):
            cad = cad +" "+ str(self.__a[i])
        for i in range(len(self.__b)):
            cad = cad + " "+str(self.__b[i])
        print(cad)
    
    def verPerpendicu(self,otro):
        suma = []
        resta = []
        for i in range(len(self.__a)):
            suma.append((self.__a[i]+self.__b[i]))

        for i in range(len(self.__a)):
            resta.append((self.__a[i]-self.__b[i]))

        moduloSum = 0
        for i in range(len(self.__a)):
            moduloSum = moduloSum+ (suma[i]**2)
        #print(f"moddulo sum: {moduloSum}")
        moduloSum = moduloSum **(0.5)
        
        moduloRes = 0
        for i in range(len(self.__a)):
            moduloRes = moduloRes +(resta[i]**2)
            #print(resta[i])
        #print(moduloRes)
        moduloRes = moduloRes **(0.5)
        
        if (moduloSum == moduloRes):
            print ("Si son perpendiculares")
        else:
            print (moduloSum, moduloRes)
    def verParalelo(self):
        result = []
        for i in range(len(self.__a)):
            result.append((self.__a[i]/self.__b[i]))
        sw = True
        for i in range(len(self.__a)-1):
            if (result[i] == result[i+1]):
                sw = True
            else:
                sw = False
                break
        if (sw == True ):
            print("son paralelos")
        else:
            print("no son paralelos")
        
    
        
class main():
    a = ([4,0,0])
    b = ([0,3,0])
    v1 = AlgebraVectorial()
    v2 = AlgebraVectorial()
    for i in range(len(a)):
        v1.agregarA(a[i])
    for i in range(len(b)):
        v1.agregarB(b[i])
    v1.mostrar()
    
    v1.verPerpendicu(v2)
    
    v1.verParalelo()
    