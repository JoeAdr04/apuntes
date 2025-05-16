class Trabajador:
    def __init__(self, salario):
        self._salario = salario
        
    def __str__(self):
        return (f"salario :{self._salario}")
class Persona:
    def __init__(self, nombre, ci):
        self._nombre = nombre
        self._ci = ci
        
    def __str__(self):
        return (f"nombre :{self._nombre}, ci: {self._ci}")
    
    def getNombre(self):
        return self._nombre
class Policia(Trabajador, Persona):
    def __init__(self, salario, nombre, ci, rango):
        Trabajador.__init__(self,salario)
        Persona.__init__(self,nombre, ci)
        self.__rango = rango
    def __str__(self):
        cad = Trabajador.__str__(self) + Persona.__str__(self)
        return (f"{cad}, rango: {self.__rango}" )
    
    def getRango(self):
        return self.__rango

class RetenPolicial:
    def __init__(self, zona):
        self.__ubicacion = zona
        self.__nroPolicias = 0
        self.__Policias = []
        
    def agregarPolicia(self,aux):
        self.__Policias.append(aux)
        self.__nroPolicias =self.__nroPolicias+1
    
    def __str__(self):
        cad = f"zona: {self.__ubicacion}"
        for i in range(self.__nroPolicias):
            cad = cad+" Policia"+(self.__Policias[i].__str__())+"\n"
        return (cad)
    
    def getNombPolicias(self):
        vec = []
        for i in range(self.__nroPolicias):
            vec.append((self.__Policias[i]).getNombre())
        return vec
    
    def getRangos(self):
        vec = []
        for i in range(self.__nroPolicias):
            vec.append((self.__Policias[i]).getRango())
        return vec
    
    def getPolicias(self):
        vec = []
        for i in range(self.__nroPolicias):
            vec.append((self.__Policias[i]))
        return vec
    
    def setPolicias(self, x):
        self.__Policias = x
    
    def getPorRango(self, x):
        for i in range(self.__nroPolicias):
            if (x == self.__Policias[i].getRango()):
                return self.__Policias[i]
            
    def buscaPoli(self, poli):
        for i in range(self.__nroPolicias):
            if(self.__Policias[i] == poli):
                return f"zona :{self.__ubicacion}"
            
    def getUbicacion(self):
        return self.__ubicacion
class Distrito:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__nroRetenes = 0
        self.__Retenes = []
        
    def agregarReten(self, reten):
        self.__Retenes.append(reten)
        self.__nroRetenes = self.__nroRetenes+1
        
    def __str__(self):
        cad = f"NombreDistrito: {self.__nombre}\n"
        for i in range(self.__nroRetenes):
            cad = cad+"Reten"+(self.__Retenes[i].__str__())+"\n"
        return (cad)
    
    def mostrar(self, x):
        for reten in self.__Retenes:
            nombres = reten.getNombPolicias()
            if x not in nombres:
                print(reten)
    
    def mostrarRrango(self, x):
        for reten in self.__Retenes:
            rangos  = reten.getRangos()
            for i in range (len(rangos)):
                if(x == rangos[i]):
                    print(reten.getPorRango(x))
    
    def buscarPolicia(self, poli):
        for reten in self.__Retenes:
            policias = reten.getPolicias()
            for i in range(len(policias)):
                if (policias[i] == poli):
                    print(reten.getUbicacion())
                    
    
    def intercambiar(self,x,y):
        aux1 = []
        aux2 = []
        for reten in self.__Retenes:
            if(reten.getUbicacion()==x):
                aux1 = reten.getPolicias()
        for reten in self.__Retenes:
            if(reten.getUbicacion()==y):
                aux2= reten.getPolicias()
        if (len(aux1)!=0 and len(aux2)!=0):
            for reten in self.__Retenes:
                if(reten.getUbicacion()==x):
                    reten.setPolicias(aux2)
            for reten in self.__Retenes:
                if(reten.getUbicacion()==y):
                    reten.setPolicias(aux1)

class Main():  
    p1 = Policia(1234, "jose", 3456, "mayor")
    p2 = Policia(3456, "juana", 567, "sargento")
    p3 = Policia(3456, "luis", 567, "subOfical")
    p4 = Policia(3456, "ignacio", 567, "teniente")
    #print(p1)
    
    r1 = RetenPolicial("achocalla")
    r2 = RetenPolicial("sorata")
    
    #print(r1)
    r1.agregarPolicia(p2)
    r1.agregarPolicia(p1)
    r2.agregarPolicia(p3)
    r2.agregarPolicia(p4)
    #print(r1)
    
    d1 = Distrito("distrito 9")
    d1.agregarReten(r1)
    d1.agregarReten(r2)
    #print(d1)
    d1.mostrar("luis")
    #d1.mostrarRrango("sargento")}
    #d1.buscarPolicia(p1)
    #print(d1)
    d1.intercambiar("sorata","achocalla")
    #print(d1)