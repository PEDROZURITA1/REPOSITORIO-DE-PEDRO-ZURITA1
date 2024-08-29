class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print(f"El producto con ID {producto.id_producto} ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto {producto.nombre} agregado al inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado del inventario.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as file:
            for producto in self.productos.values():
                file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio:.2f}\n")
        print(f"Inventario guardado en {nombre_archivo}.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.agregar_producto(producto)
            print(f"Inventario cargado desde {nombre_archivo}.")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")


def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad o precio")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no se actualiza): ")
            precio = input("Nuevo precio (dejar vacío si no se actualiza): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            nombre_archivo = input("Nombre del archivo donde guardar el inventario: ")
            inventario.guardar_en_archivo(nombre_archivo)

        elif opcion == "7":
            nombre_archivo = input("Nombre del archivo desde donde cargar el inventario: ")
            inventario.cargar_desde_archivo(nombre_archivo)

        elif opcion == "8":
            print("Saliendo del sistema de gestión de inventario.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
