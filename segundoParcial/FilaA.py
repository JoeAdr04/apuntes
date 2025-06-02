class Anuncio:
    def __init__(self, numero = 0, precio = 0):
        self.__numero = numero
        self.__precio = precio
    
    def __str__(self):
        return (f"Numero : {self.__numero}, precio: {self.__precio}")
    
    def getPrecio(self):
        return self.__precio
    
class Artista:
    def __init__(self, nombre = "", ci ="", aniosExp = 0):
        self.__nombre = nombre
        self.__ci = ci
        self.__aniosExp = aniosExp
    
    def __str__(self):
        return (f"Nombre: {self.__nombre}, Ci: {self.__ci}, Anios de Experiencia: {self.__aniosExp}")
    
    def getAniosExp(self):
        return self.__aniosExp
    
class Obra:
    def __init__(self, titulo="", material="",nombre1="", ci1="", aniosExp1=0,nombre2="", ci2="", aniosExp2=0):
        self._titulo = titulo
        self._material = material
        self._artista1 = Artista(nombre1, ci1, aniosExp1)
        self._artista2 = Artista(nombre2, ci2, aniosExp2)
        self._anuncio = Anuncio()
        
    def __str__(self):
        return (f"Titulo: {self._titulo}, Material: {self._material}\nArtista1: ({self._artista1})\nArtista2: ({self._artista2})\nAnuncio: ({self._anuncio})")
    
    def agregarAnuncio(self, a1):
        self._anuncio = a1
        
    
    
class Pintura(Obra):
    def __init__(self, titulo="", material="", genero="", nombre1="", ci1="", aniosExp1=0, nombre2="", ci2="", aniosExp2=0):
        super().__init__(titulo, material, nombre1, ci1, aniosExp1, nombre2, ci2, aniosExp2)
        self.__genero = genero
        
    def __str__(self):
        return (f"Genero: {self.__genero}, {super().__str__()}")
    
    def masAniosExp(self, otraPintura:Obra):
        mayor = 0
        artista = Artista()
        artistas = [self._artista1, self._artista2, otraPintura._artista1, otraPintura._artista2]
        for i in range (len(artistas)-1):
            if (artistas[i].getAniosExp()>mayor):
                mayor = artistas[i].getAniosExp()
                artista = artistas[i]
        return artista
    
class Main():
    print("------Incicso a-----------")
    p1 = Pintura("Monaliza", "oleo","romance","picasso", 12341, 12, "leonardo", 4567, 10)
    a1 = Anuncio(12345, 123.5)
    p1.agregarAnuncio(a1)
    
    p2 = Pintura("campanella", "acuarela", "terror", "gustavo", 87654, 2, "cerati", 765, 4)
        
    print (p1)
    print (p2)
    print("-----------Inciso b -----------")
    print(f"Artista con mas anios de exp: {p1.masAniosExp(p2)}")
    
    print("-----------Inciso c -----------")
    a2 = Anuncio(34567, 456.23)
    p2.agregarAnuncio(a2)
    print(f"Monto total: {a1.getPrecio()+a2.getPrecio()}")