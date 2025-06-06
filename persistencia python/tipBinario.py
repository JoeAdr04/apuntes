import pickle
import os

class Empleado:
    # Clase que representa un empleado con nombre, carnet y fecha de nacimiento.
    def __init__(self, nombre, carnet, fecha_nac):
        self.nombre = nombre
        self.carnet = carnet
        self.fecha_nac = fecha_nac

    def get_carnet(self):
        # Devuelve el carnet del empleado.
        return self.carnet

    def __str__(self):
        # Representación en texto del empleado.
        return f"Nombre: {self.nombre}, Carnet: {self.carnet}, Fecha Nac: {self.fecha_nac}"

class ArchEmpleado:
    # Clase para manejar la persistencia de empleados en un archivo binario usando pickle.
    def __init__(self, filename="arch.dat"):
        self.filename = filename

    def guardar(self, empleado):
        # Guarda un empleado en el archivo binario.
        try:
            empleados = self.listar()
            empleados.append(empleado)
            with open(self.filename, "wb") as f:
                pickle.dump(empleados, f)
        except Exception as e:
            print(f"Error al guardar empleado: {e}")

    def listar(self):
        # Lista todos los empleados guardados en el archivo binario.
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []
        except Exception as e:
            print(f"Error al listar empleados: {e}")
            return []

    def eliminar(self, carnet):
        # Elimina un empleado por su carnet. Retorna True si se eliminó, False si no se encontró.
        try:
            empleados = self.listar()
            nuevos = []
            eliminado = False
            for emp in empleados:
                if emp.get_carnet() != carnet:
                    nuevos.append(emp)
                else:
                    eliminado = True
            with open(self.filename, "wb") as f:
                pickle.dump(nuevos, f)
            return eliminado
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False

    def editar(self, carnet, nuevo_nombre, nueva_fecha_nac):
        # Edita los datos de un empleado identificado por su carnet. Retorna True si se editó, False si no se encontró.
        try:
            empleados = self.listar()
            editado = False
            for emp in empleados:
                if emp.get_carnet() == carnet:
                    emp.nombre = nuevo_nombre
                    emp.fecha_nac = nueva_fecha_nac
                    editado = True
            with open(self.filename, "wb") as f:
                pickle.dump(empleados, f)
            return editado
        except Exception as e:
            print(f"Error al editar empleado: {e}")
            return False

def menu():
    # Menú de consola para gestionar empleados en archivo binario.
    arch = ArchEmpleado()
    while True:
        print("\n--- Menú Empleados Binario ---")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Eliminar empleado por carnet")
        print("4. Editar empleado por carnet")
        print("5. Salir")
        op = input("Seleccione una opción: ")
        if op == "1":
            try:
                nombre = input("Nombre: ")
                carnet = input("Carnet: ")
                fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
                emp = Empleado(nombre, carnet, fecha_nac)
                arch.guardar(emp)
                print("Empleado guardado.")
            except Exception as e:
                print(f"Error al agregar empleado: {e}")
        elif op == "2":
            try:
                empleados = arch.listar()
                if not empleados:
                    print("No hay empleados registrados.")
                else:
                    for emp in empleados:
                        print(emp)
            except Exception as e:
                print(f"Error al listar empleados: {e}")
        elif op == "3":
            carnet = input("Carnet del empleado a eliminar: ")
            if arch.eliminar(carnet):
                print("Empleado eliminado.")
            else:
                print("Empleado no encontrado o error al eliminar.")
        elif op == "4":
            carnet = input("Carnet del empleado a editar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_fecha_nac = input("Nueva fecha de nacimiento (YYYY-MM-DD): ")
            if arch.editar(carnet, nuevo_nombre, nueva_fecha_nac):
                print("Empleado editado.")
            else:
                print("Empleado no encontrado o error al editar.")
        elif op == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()