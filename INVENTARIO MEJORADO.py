import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(",")
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.productos[id_producto] = producto
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado. Creando un nuevo archivo...")
            self.guardar_inventario()
        except Exception as e:
            print(f"Error al cargar inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(f"{producto.get_id_producto()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Error: No tienes permisos para escribir en '{self.archivo}'.")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def añadir_producto(self, producto):
        if producto.get_id_producto() in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.get_id_producto()] = producto
            self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto(s)")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")


if __name__ == "__main__":
    menu()
