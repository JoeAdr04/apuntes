import json

class Empleado:
    #clase empleado
    def __init__(self, nombre, carnet, fecha_nac):
        self.nombre = nombre
        self.carnet = carnet
        self.fecha_nac = fecha_nac

    def to_dict(self): #convierte el objeto a un diccionario
        return {
            "nombre": self.nombre,
            "carnet": self.carnet,
            "fecha_nac": self.fecha_nac
        }

class ArchEmpleado: #clase para manejar el archivo de empleados
    def __init__(self, filename="arch.json"): #constructor que recibe el nombre del archivo
        self.filename = filename

    def guardar(self, empleado): #guarda un empleado en el archivo JSON
        datos = self.listar()
        datos.append(empleado.to_dict())
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    def listar(self): #lista todos los empleados del archivo JSON
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def eliminar(self, carnet): #elimina un empleado por su carnet
        datos = self.listar()
        nuevos = []
        eliminado = False #retornara un false en casod e no eliminar
        for emp in datos:
            if emp["carnet"] != carnet: #si el carnet no coincide, lo agrega a la lista nueva
                nuevos.append(emp)
            else:
                eliminado = True
        with open(self.filename, "w", encoding="utf-8") as f: #escribe los datos nuevos en el archivo
            json.dump(nuevos, f, ensure_ascii=False, indent=4) #.dump convierte la lista a JSON
        return eliminado

    def editar(self, carnet, nuevo_nombre, nueva_fecha_nac): #edita un empleado por su carne
        datos = self.listar() 
        editado = False
        for emp in datos:
            if emp["carnet"] == carnet: #si el carnet coincide, edita los datos
                emp["nombre"] = nuevo_nombre
                emp["fecha_nac"] = nueva_fecha_nac
                editado = True
        with open(self.filename, "w", encoding="utf-8") as f: # escribe los datos editados en el archivo
            json.dump(datos, f, ensure_ascii=False, indent=4)
        return editado
#Necesitaremos una forma de evitar redundancia cada ves que se ejcute el codigo
# y que el archivo se cree si no existe, por lo que crearemos una funcion para el menu

def menu(): #funcion para mostrar el menu y manejar las opciones
    
    arch = ArchEmpleado() #archivo de empleados
    while True:
        print("\n--- Menú Empleados ---")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Eliminar empleado por carnet")
        print("4. Editar empleado por carnet")
        print("5. Salir")
        op = input("Seleccione una opción: ") #opción del menú
        if op == "1":
            nombre = input("Nombre: ")
            carnet = input("Carnet: ")
            fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
            emp = Empleado(nombre, carnet, fecha_nac)
            arch.guardar(emp)
            print("Empleado guardado.")
        elif op == "2":
            empleados = arch.listar()
            if not empleados:
                print("No hay empleados registrados.")
            else:
                for emp in empleados:
                    print(f"Nombre: {emp['nombre']}, Carnet: {emp['carnet']}, Fecha Nac: {emp['fecha_nac']}")
        elif op == "3":
            carnet = input("Carnet del empleado a eliminar: ")
            if arch.eliminar(carnet):
                print("Empleado eliminado.")
            else:
                print("Empleado no encontrado.")
        elif op == "4":
            carnet = input("Carnet del empleado a editar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_fecha_nac = input("Nueva fecha de nacimiento (YYYY-MM-DD): ")
            if arch.editar(carnet, nuevo_nombre, nueva_fecha_nac):
                print("Empleado editado.")
            else:
                print("Empleado no encontrado.")
        elif op == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu() #llama a la funcion menu si se ejecuta el script directamente
