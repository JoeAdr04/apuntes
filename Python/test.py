from multimethod import multimethod

@multimethod
def saludar(nom: str):
    print(f"hola, {nom} como estas")

@multimethod
def saludar(nom: str, edad: int):
    print(f"hola {nom}, tienes {edad} años")


nombre = "jose"
edad = 14

saludar(nombre)
print("/////////////////")
saludar("juana", edad)