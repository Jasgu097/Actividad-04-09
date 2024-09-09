#Jason Misael Gutierrez de Leon 1624622
import pickle

class Cliente:
    def __init__(self, nombre, email, fecha_ultimo_contacto):
        self.nombre = nombre
        self.email = email
        self.fecha_ultimo_contacto = fecha_ultimo_contacto

class ArchivoSecuencial:
    def __init__(self, archivo_nombre):
        self.archivo_nombre = archivo_nombre

    def agregar_cliente(self, cliente):
        # Modo append para agregar más clientes sin sobrescribir
        with open(self.archivo_nombre, "ab") as archivo:
            pickle.dump(cliente, archivo)
        print(f"Cliente {cliente.nombre} agregado al archivo binario.")

    def mostrar_clientes(self):
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

archivo = ArchivoSecuencial("clientes_secuencial.bin")

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
archivo.mostrar_clientes()
