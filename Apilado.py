#Jason Misael Gutierrez de Leon 1624622
import pickle

class Cliente:
    def __init__(self, nombre, email, fecha_ultimo_contacto):
        self.nombre = nombre
        self.email = email
        self.fecha_ultimo_contacto = fecha_ultimo_contacto

class PilaClientes:
    def __init__(self, archivo_nombre):
        self.pila = []
        self.archivo_nombre = archivo_nombre

    def agregar_cliente(self, cliente):
        self.pila.append(cliente)
        print(f"Cliente {cliente.nombre} agregado a la pila.")

    def quitar_cliente(self):
        if self.pila:
            cliente = self.pila.pop()
            print(f"Cliente {cliente.nombre} removido de la pila.")
            return cliente
        else:
            print("La pila está vacía.")
            return None

    def agregar_cliente_archivo(self):
        with open(self.archivo_nombre, "ab") as archivo:
            for i in self.pila:
                pickle.dump(i, archivo)
                print(f"Cliente {i.nombre} agregado al archivo binario.")

    def mostrar_clientes(self):
        print("Clientes en la pila:")
        for cliente in reversed(self.pila):
            print(f"Nombre: {cliente.nombre}, Email: {cliente.email}, Último contacto: {cliente.fecha_ultimo_contacto}")

    def mostrar_archivo(self):
        print("Clientes en el archivo binario:")
        try:
            with open(self.archivo_nombre, "rb") as archivo:
                while True:
                    try:
                        cliente = pickle.load(archivo)
                        print(f"Nombre: {cliente.nombre}, Email: {cliente.email}, Último contacto: {cliente.fecha_ultimo_contacto}")
                    except EOFError:
                        break
        except FileNotFoundError:
            print("El archivo binario no existe.")

# Ejemplo de uso
archivo = PilaClientes("clientes_pila.bin")

def main():
    while True:
        print("Ingrese la informacion del clientes. ")
        nombre = input("Ingrese el nombre del cliente: ")
        email = input("Ingrese el correo electronico del cliente: ")
        fecha = input("Fecha que se envio la informacion: ")

        cliente = Cliente(nombre, email, fecha)

        archivo.agregar_cliente(cliente)
        opcion = int(input("Desea almacenar otros datos?: \n1. Si \n2. No\n"))
        if opcion == 1:
            print("--------------------")
        elif opcion == 2:
            print("Saliendo...")
            break
        else:
            print("Opcion no Valida, intentelo de nuevo...")

main()
archivo.agregar_cliente_archivo()
archivo.mostrar_archivo()
