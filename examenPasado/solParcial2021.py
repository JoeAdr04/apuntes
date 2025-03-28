'''
se requiere desarrollar un diagrama de clases para un sistema que administra maratones.Cada 
maraton debe registrar un nombre, la fecha de realizacion, y el lugar donde se llevara acabo.
Cada maraton tiene un unico organizador que es la persona responsable del evento e indispensable
para su realizacion. De este organizador se desea saber su nombre, edad ,egenero y numero de telefono
ademas cada maraton tiene una lista de varias carreras. De cada carrera se necesita registrar la hora 
de inicio, la longitud del recorrido y se debe mantener una lista de los corredores inscritos en la
competicion. De cada corredor se desea almacenar su nombre, dedad, genero, y el numero asignado para 
la competicion. Adicionalmente para finalizar cada evento se otorgan medallas a los corredores, por 
lo que se debe considerar tambien en el sistema, cada medalla debe incluir el numero asignado al 
corredor, la categoria y el año en que se otorgo.
Diseña el diagrama de clases correspondiente a este sistema, asi como las relaciones entre ellas.

Problemas para resolver en el laboratorio:
a) Implementar todas las clases con sus respectivos constructores y algun metodo para 
mostrar datos(4 pts.)
b)Instanciar 1 maraton , 2 Carreras  y 4 corredores, ademas de 2 medallas. (2 pts.)
c)Sobrecargar el operador (-) para agregar corredores a una Carrera.(2 pts.)
d) Sobrecargar el operador (+) ara agregare carreras a una maraton. (2 pts.)
e) A cada carrera agregar 2 corredores y agregar las dos carreras a la maraton y mostrar la 
Maraton(2 pts.)
f) Crear un metodo para verificar si en la carrera con longitud de recorrido x se encuentra el coredor 
con nombre y. (2 pts.)
g) Crear un metodo para verifica si en la maraton algun corredor es menor de edad (2 pts.)
h) Crear un metodo para mostrar el nombre de los corredores que ganaron alguna medalla (2 pts.)
i) Crear un metodo que devuelva la cantidad de corredores del genero "femenino" en toda la
Maraton (2 pts.)

'''
#clases Maraton, Carrera, Medalla, Organizador, Corredor
# Herencia : Persona = (Organizador/Corredor) (atributos en comun: nombre, edad, genero)
#Composicion: Maraton <<-Organizador (el organizador es indispensable para la maraton)
# Agregacion: Maraton <- Carrera / Carrera <- Corredor
# Asociacion: Corredor -- Medalla

class Persona:
    def __init__(self, nombre, edad, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero =  genero
    
    def __str__(self):
        return f"Nombre : {self.__nombre}, Edad: {self.__edad}, Genero: {self.__genero}"
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getGenero(self):
        return self.__genero
    
class Organizador(Persona):
    def __init__(self, nombre, edad, genero, nroTelefono):
        super().__init__(nombre,edad,genero)
        self.__nroTelefono = nroTelefono
    
    def __str__(self):
        cad = super().__str__() # guardo el valor de la cadena que retorna el __str__ padre
        return f"{cad}, NroTelefono: {self.__nroTelefono}"

class Corredor(Persona):
    def __init__(self, nombre, edad, genero, nroAsig):
        super().__init__(nombre,edad,genero)
        self.__nroAsig = nroAsig
    
    def __str__(self):
        cad = super().__str__()
        return f"{cad}, Nro Asignado: {self.__nroAsig}"
    
    def getNro(self):
        return self.__nroAsig
    
class Maraton:
    def __init__(self, Organizador:Organizador, nombre, fecha, lugar):
        self.__Organizador = Organizador
        self.__nombre = nombre
        self.__fecha = fecha
        self.__lugar = lugar
        self.__carreras =[]
        
    def __add__(self, carrera):
        if(isinstance(carrera, Carrera)):
            self.__carreras.append(carrera)
        else:
            print("Solo se puede agregar carreras")
    
    def __str__(self):
        return (f"Maraton :{self.__nombre}\nFecha: {self.__fecha}\nLugar: {self.__lugar} \nOrganizador: ({self.__Organizador})")
    
    def verificar(self, x,y):
        for i in range(len(self.__carreras)):
            if(self.__carreras[i].getLongitud() == x):
                vec = self.__carreras[i].getList()
                for j in range (len(vec)):
                    if(vec[j].getNombre() == y):
                        return True
                    else:
                        return False
                    
    def contarF(self):
        contador = 0
        for i in range(len(self.__carreras)):
            vec = self.__carreras[i].getList()
            for j in range (len(vec)):
                if(vec[j].getGenero() == "Femenino" or vec[j].getGenero() == "femenino" or vec[j].getGenero() == "FEMENINO"):
                    contador = contador +1
        return contador
    
    def verficaEdad(self):
        menores = ""
        for i in range(len(self.__carreras)):
            
            vec = self.__carreras[i].getList()
            for j in range (len(vec)):
                if(vec[j].getEdad() <18):
                    menores = menores +" "+ vec[j].getNombre()
        if (menores == ""):
            return "No se encontraron menores"
        else:
            
            return (f"Menores ecnontrados: \n{menores}")
        
    def verMedallas(self, nro):
        for i in range(len(self.__carreras)):
            
            vec = self.__carreras[i].getList()#obtiene lista de corredores d ela carrera iesima
            for j in range (len(vec)):
                if (vec[j].getNro() == nro):
                    return True
        return False

    def corredorPorNumero(self, num):
        for i in range(len(self.__carreras)):
            vec = self.__carreras[i].getList()#obtiene lista de corredores d ela carrera iesima
            for j in range (len(vec)):
                if (vec[j].getNro() == num):
                    return vec[j].getNombre()
class Carrera:
    def __init__(self, horaInic, longitud):
        self.__horaInic = horaInic
        self.__longitud = longitud
        self.__corredores = []
        
    def __str__(self):
        cadena = "\n".join(str(c) for c in self.__corredores)
        return (f"Hora Incio: {self.__horaInic}, Longitud: {self.__longitud}\n Corredores:\n {cadena}")
    
    def __sub__(self, corredor): #agregar corredor a una carrera
        if (isinstance(corredor, Corredor)):
            self.__corredores.append(corredor)
        else:
            print("solo se puede agregar corredores")
    
    def getLongitud(self):
        return self.__longitud
    
    def getList(self):
        return self.__corredores
    
class Medalla:
    def __init__(self, numCorredor, categoria, anio):
        self.__numero = numCorredor
        self.__categoria = categoria
        self.__anio = anio
        
    def __str__(self):
        return (f"Corredor Nro: {self.__numero}, Categoria: {self.__categoria}, Año: {self.__anio}")
    
    def getNum(self):
        return self.__numero
    
class main():
    
    organizador = Organizador("jose",22, "Masculino", 12341234)
    maraton = Maraton(organizador, "Pedestre", "21/02/18", "viacha")
    carrera1 = Carrera("08:00",1234.5)
    carrera2 = Carrera("12:00", 234.56)
    corredor1 = Corredor("pedro", 15, "Masculino", 4)
    corredor2 = Corredor("maria", 16, "Femenino", 44)
    corredor3 = Corredor("chaski", 34, "femenino", 34)
    corredor4 = Corredor("paola", 17, "Femenino", 12)
    medalla1= Medalla(44,"oro",2017)
    medalla2= Medalla(4, "plata", 2022)
    carrera1 - corredor1
    carrera1 - corredor2
    #carrera1.agregarCorredor(corredor2)
    carrera2 - corredor3
    carrera2 - corredor4
    #carrera2.agregarCorredor(corredor4)
    maraton + carrera1
    maraton + carrera2
    
    print(maraton)
    
    if (maraton.verificar(234.56, "chaski")):
        print("ALCH si se encuentra, ya verifique")
    else:
        print ("No lo encontre bro")
    
    print(maraton.verficaEdad())

    medallero = [medalla1,medalla2]
    ganadores  = ""
    for i in range(len(medallero)):
        if (maraton.verMedallas(medallero[i].getNum())):
            ganadores = ganadores +"\n"+ maraton.corredorPorNumero(medallero[i].getNum())
    
    print (f"Los ganadores son: \n{ganadores}")
    
    print(f"la cantida de corredoras del genero femenino es: {maraton.contarF()}")