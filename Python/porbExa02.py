#pip install multimethod
from multimethod import multimethod

class Cine:
    def __init__(self, nombre="", direccion="", cantPeliculas= 0):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__cantPeliculas = cantPeliculas
        self.__peliculas = ["el aro", "shrek", "transformers", "pacificRim","joelAdrianTraqui","asdf","qwer","zxcv","45","fhkd"]
        self.__generos = ["terror","comedia","cficcion","comedia","comedia","asdf","asdf","asdf","asdf","asdf"]
        self.__precioButaca = [12.3,4.3, 345.4, 34.2,12.3,4.3, 345.4, 34.2, 4.2, 4.4]
    
    def leer(self):
        self.__nombre = str(input("ingresa nombre: "))
        self.__direccion = str(input("ingresa direccion: "))
        self.__cantPeliculas = int(input("ingresa cantpeliculas: "))
    
    def __str__(self):
        cad = f"nombre: {self.__nombre}, direccion: {self.__direccion}, cantPeliculas: {self.__cantPeliculas}\n"
        for i in range(len(self.__peliculas)):
            cad = cad +(f"nomPelicula: {self.__peliculas[i]}, genero: {self.__generos[i]}, precio: {self.__precioButaca[i]}\n")
        return (cad)
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    @multimethod    
    def mostrar(self):
        cad = "Peliculas genero comedia: \n"
        for i in range(len(self.__peliculas)):
            if(self.__generos[i] == "comedia"):
                cad = cad +(f"nomPelicula: {self.__peliculas[i]}, genero: {self.__generos[i]}, precio: {self.__precioButaca[i]}\n")
        print(cad)
        
    @multimethod
    def mostrar(self, i:int):
        print (f"nomPelicula: {self.__peliculas[i-1]}, genero: {self.__generos[i-1]}, precio: {self.__precioButaca[i-1]}\n")
    
    def __iadd__(self, otro):
        if (isinstance(otro, int)):
            for i in range(len(self.__peliculas)):
                self.__precioButaca[i] = self.__precioButaca[i]+otro
            return self
        else:
            return self
        
    def ordenar(self):
        n = self.__cantPeliculas
        for i in range(n-1):
            for j in range(n-1-i):
                if(self.__peliculas[j]> self.__peliculas[j+1]):
                    self.__peliculas[j], self.__peliculas[j+1] = self.__peliculas[j+1],self.__peliculas[j]
                    self.__generos[j], self.__generos[j+1] = self.__generos[j+1],self.__generos[j]
                    self.__precioButaca[j], self.__precioButaca[j+1] = self.__precioButaca[j+1],self.__precioButaca[j]
                    
    
class main():
    
    cine01 = Cine("multicine", "av.arce",10)
    #print(cine01)
    #cine01.mostrar()
    #cine01.mostrar(3)
    #print(cine01)
    cine01 += 5
    
    #print(cine01)
    
    cine01.ordenar()
    print(cine01)
    
    