'''
Realiza la abstracción de un Banco que atiende a 10 usuarios con cuenta de ahorros

a)Crea un método para agregar un usuario
b)Realiza un método para que un usuario pueda retirar dinero del banco
c)Realiza un método para que un usuario pueda guardar dinero en el banco
d)Dales a los usuarios un 2% de bono en sus cuentas respecto a su saldo

Atributos de un banco
nombre del banco
caja de ahorros(double) //tesoro del banco
usuarios[nombres]
cuenta[ahorros]
'''
class Banco:
    
    def __init__(self,nombre,tesoro):
        self.nombre = nombre
        self.usuarios = (["juan","maria","pepe","asdf","qwer","luis","pancho","mariana","lucas","eufacio",])
        self.cuenta = ([1234.0,345.7,1234.7,456.12,1234.0,345.7,1234.7,456.12,1234.0,345.7])
        self.tesoro = tesoro
        
    def agregarUsuario(self, nombre, cuenta):#método para agregar un usuario
        for i in range(0,len(self.usuarios)):
            if(self.usuarios[i]==nombre):
                print("el ususario ya existe")
            else:
                self.usuarios.append(nombre)
                self.cuenta.append(cuenta)
                self.tesoro=self.tesoro+cuenta
                break  
    def retirar(self,nombre, retiro):#método para que un usuario pueda retirar dinero del banco
        for i in range(0,len(self.usuarios)):
            if(self.usuarios[i]==nombre):
                if(retiro<=self.cuenta[i]):
                    self.cuenta[i]=self.cuenta[i]-retiro
                    self.tesoro =self.tesoro-retiro
                    print(f"usted ha retirado {retiro} bs.")
                else:
                    print(f"usuario {nombre} no cuenta con ese dinero")
    def guardar(self,nombre, abono):
        for i in range(0,len(self.usuarios)):
            if(self.usuarios[i]==nombre):
                self.cuenta[i]=self.cuenta[i]+abono
                print(f"usted ha depositado {abono} bs.")
            
    def darBono(self):
        for i in range(0,len(self.usuarios)):
            self.cuenta[i]= self.cuenta[i]*(1.02)#ponerle 1 le aumenta el porcentaje
    def __str__(self):
        return f'Nombre: {self.nombre} Tesoro: {self.tesoro}'
    
    def mostrarUsuarios(self):
        for i in range(0,len(self.usuarios)):
            print(f'usuario: {self.usuarios[i]} cuenta:{self.cuenta[i]} bs. \n')

class main():
    
    banco = Banco("bisa",99999.99)
    print(banco)
    
    banco.agregarUsuario("IVAN ", 23000.00)
    print(banco)
    banco.mostrarUsuarios()
    
    banco.retirar("luis", 344)
    #banco.mostrarUsuarios()
    
    banco.guardar("juan",4)
    #banco.mostrarUsuarios()
    
    banco.darBono()
    banco.mostrarUsuarios()
    