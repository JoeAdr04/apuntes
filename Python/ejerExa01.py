class Fiesta:
    def __init__(self,fecha,nombre):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__Invitados = [] #nombresInvitados :string
        self.__edad = [] # edades Invitados :int
        self.__estado = []  #estado(vip, no vip) :boolean

    def __str__(self):
        cad = ""
        cad  = "nombre: "+ self.__nombre + "Fecha:"+ self.__fecha +" Invitados:"
        for i in range(len(self.__Invitados)):
            cad = cad + f"\n {self.__Invitados[i]}"
            cad = cad + f" {self.__edad[i]}"
            cad = cad + f" {self.__estado[i]}"
        return cad
    
    def agregar(self, nombre, edad, estado):
        self.__Invitados.append(nombre)
        self.__edad.append(edad)
        self.__estado.append(estado)
        
    def __add__(self, unaCosa):
        if (isinstance(unaCosa, str)):
            for i in range(0, len(self.__Invitados)-1):
                if(unaCosa == self.__Invitados[i]):
                    #del self.__Invitados[i]
                    #del self.__edad[i]
                    #del self.__estado[i]
                    self.__Invitados.pop(i)
                    self.__edad.pop(i)
                    self.__estado.pop(i)
            return self
        else:
            nombre, edad, estado = unaCosa
            self.__Invitados.append(nombre)
            self.__edad.append(edad)
            self.__estado.append(estado)
            return self
        
    
    def eliminar(self, nombre):
        for i in range(0, len(self.__Invitados)-1):
            if(nombre == self.__Invitados[i]):
                #del self.__Invitados[i]
                #del self.__edad[i]
                #del self.__estado[i]
                self.__Invitados.pop(i)
                self.__edad.pop(i)
                self.__estado.pop(i)
    
    def ordenar(self):
        #[5,3,2,7,2]
        n = len(self.__Invitados)
        for i in range(n-1):
            for j in range(n-1-i):
                if(self.__edad[j]> self.__edad[j+1]):
                    self.__edad[j], self.__edad[j+1] = self.__edad[j+1],self.__edad[j]
                    self.__Invitados[j], self.__Invitados[j+1] = self.__Invitados[j+1],self.__Invitados[j]
                    self.__estado[j], self.__estado[j+1] = self.__estado[j+1],self.__estado[j]
                    
    
    def verVIp(self):
        for i in range(0, len(self.__Invitados)-1):
            if(self.__estado[i]):
                return True
        return False
            
        
    def __eq__(self, otra):
        for i in range(0, len(self.__Invitados)-1):
            for j in range ((i+1), len(self.__Invitados)):
                if(self.__Invitados[i] == self. __Invitados[j]):
                    return True
        return False
    
    def masJoven(self):
        men = 10
        pos = -1
        for i in range(0, len(self.__Invitados)-1):
            if(self.__edad[i] < 0):
                men = self.__edad
                pos = i
            
        print(f"invitado mas joven: {self.__Invitados[pos]}")
        
    def contarVip(self):
        dont = 0
        for i in range (0, len(self.__Invitados)-1):
            if (self.__estado[i] == True):
                dont = dont+1
        print (f"existen {dont} vips")
        
class main():
    f1 = Fiesta("20/04/2017", "gran poder")
    f1.agregar("mario", 12, False)
    f1 + ("jose", 27, True)
    f1 + ("maria", 18, True)
    f1 + ("juan", 33, False)
    f1 + ("diego", 20, False)
    
    #print(f1)
    #f1.eliminar("mario")
    #f1 + "maria"
    print(f1)
    f1.ordenar()
    print(f1)
    if (f1.verVIp()):
        print("si hay almenos un vip")
    else:
        print("no existen vips")
        
    if( f1 == 2):
        print("dos tienen el mismo nombre")
    else:
        print("no hay invitados iguales")
    
    f1.masJoven()
    f1.contarVip()