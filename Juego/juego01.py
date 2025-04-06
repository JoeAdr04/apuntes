import random

class  Juego:
    def __init__(self, nroVidas):
        self._nroVidas = nroVidas
        self.__record = 0
        
    def reiniciarPartida(self):
        self._nroVidas = 3
        self.__record = 0
        
    def actualizaRecord(self):
        self.__record = self.__record+1
        
    def quitaVida(self):
        if(self._nroVidas == 0 ):
            return False
        else:
            return True
    
    def getRecord(self):
        return self.__record
    
class JuegoAdivinaNumero(Juego):
    def __init__(self, nroVidas):
        super().__init__(nroVidas)
        self.__numeroAdivinar = random.randint(0,10)
        
    def juega(self):
        super().reiniciarPartida()
        
        
        while(self.quitaVida() == True):
            print(self.__numeroAdivinar)
            numero = int(input("Ingrese un numero entre 0 y 10: "))
            if(self.__numeroAdivinar == numero):
                self.actualizaRecord()
                print(f"Acertaste! (Record = {self.getRecord()})")
                self.__numeroAdivinar = random.randint(0,10)
            else:
                self._nroVidas = self._nroVidas-1
                print(f"Intentalo de nuevo \n te quedan {self._nroVidas} vidas")
        print("---------------------------------")
        print(f"Juego terminado \n Record: {self.getRecord()} ")
            
class main():
    print("---------ADIVINA EL NUMERO---------")
    game = JuegoAdivinaNumero(3)
    game.juega()
    
#import tkinter
#wind = tkinter.Tk()
#wind.mainloop()