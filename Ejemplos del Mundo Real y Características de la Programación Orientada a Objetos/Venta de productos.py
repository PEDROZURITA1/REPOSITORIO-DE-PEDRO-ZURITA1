import datetime

# Clase Categoria para representar una categoría de productos
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase Producto para representar un producto
class Producto:
    def __init__(self, id_producto, nombre, precio, categoria, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    # Método para actualizar el stock del producto
    def actualizar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print(f"No hay suficiente stock para el producto {self.nombre}")
            return False

# Clase Cliente para representar un cliente
class Cliente:
    def __init__(self, id_cliente, nombre, apellido, direccion, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

# Clase Venta para representar una venta
class Venta:
    def __init__(self, id_venta, fecha, cliente):
        self.id_venta = id_venta
        self.fecha = fecha
        self.cliente = cliente
        self.productos = []  # Lista de productos en la venta
        self.total = 0.0  # Total de la venta

    # Método para agregar un producto a la venta
    def agregar_producto(self, producto, cantidad):
        if producto.actualizar_stock(cantidad):
            self.productos.append((producto, cantidad))

    # Método para calcular el total de la venta
    def calcular_total(self):
        self.total = sum(producto.precio * cantidad for producto, cantidad in self.productos)

    # Método para mostrar información de la venta
    def mostrar_informacion(self):
        print(f"ID de Venta: {self.id_venta}")
        print(f"Fecha: {self.fecha}")
        print(f"Cliente: {self.cliente.nombre} {self.cliente.apellido}")
        print("Productos:")
        for producto, cantidad in self.productos:
            print(f"- {producto.nombre}: {cantidad} x {producto.precio} = {cantidad * producto.precio}")
        print(f"Total: {self.total}")

# Creamos algunas categorías
categoria1 = Categoria("Alimentos")
categoria2 = Categoria("Electrónica")

# Creamos algunos productos
producto1 = Producto(1, "Leche", 2.50, categoria1, 10)
producto2 = Producto(2, "Pan", 1.20, categoria1, 6)
producto3 = Producto(3, "TV", 500.00, categoria2, 3)
producto4 = Producto(4, "Celular", 250.00, categoria2, 2)

# Creamos un cliente
cliente1 = Cliente(1, "Juan", "Pérez", "Av. 123", "123456789")

# Creamos una venta
venta1 = Venta(1, datetime.date(2024, 6, 19), cliente1)

# Agregamos productos a la venta
venta1.agregar_producto(producto1, 2)
venta1.agregar_producto(producto3, 1)

# Calculamos el total de la venta
venta1.calcular_total()

# Mostramos información de la venta
print("\nInformación de la venta:")
venta1.mostrar_informacion()
