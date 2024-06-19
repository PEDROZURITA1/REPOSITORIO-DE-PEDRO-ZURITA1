import datetime

# Clase Autor para representar un autor
class Autor:
    def __init__(self, nombre, apellido, pais):
        self.nombre = nombre
        self.apellido = apellido
        self.pais = pais

# Clase Libro para representar un libro
class Libro:
    def __init__(self, isbn, titulo, autor, cantidad, prestados):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.prestados = prestados

    # Método para prestar un libro
    def prestar(self):
        if self.cantidad > self.prestados:
            self.prestados += 1
        else:
            print(f"No hay copias disponibles del libro {self.titulo} para prestar.")

    # Método para devolver un libro
    def devolver(self):
        if self.prestados > 0:
            self.prestados -= 1
        else:
            print(f"No hay préstamos activos del libro {self.titulo} para devolver.")

    # Método para mostrar información del libro
    def mostrar_informacion(self):
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.nombre} {self.autor.apellido}")
        print(f"Cantidad total: {self.cantidad}")
        print(f"Cantidad prestados: {self.prestados}")

# Clase Prestamo para representar un préstamo de un libro
class Prestamo:
    def __init__(self, libro, fecha_prestamo, fecha_devolucion, cliente):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.cliente = cliente
        libro.prestar()

    # Método para mostrar información del préstamo
    def mostrar_informacion(self):
        print(f"Libro: {self.libro.titulo}")
        print(f"Fecha de préstamo: {self.fecha_prestamo}")
        print(f"Fecha de devolución: {self.fecha_devolucion if self.fecha_devolucion else 'No devuelto'}")
        print(f"Cliente: {self.cliente}")

# Creamos algunos autores
autor1 = Autor("Gabriel", "García Márquez", "Colombia")
autor2 = Autor("Isabel", "Allende", "Chile")

# Creamos algunos libros
libro1 = Libro("ISBN123456789", "Cien años de soledad", autor1, 5, 2)
libro2 = Libro("ISBN987654321", "El amor en los tiempos del cólera", autor1, 3, 1)
libro3 = Libro("ISBN000000001", "La casa de los espíritus", autor2, 6, 4)

# Realizamos algunos préstamos
prestamo1 = Prestamo(libro1, datetime.date(2024, 6, 15), None, "Juan Pérez")
prestamo2 = Prestamo(libro2, datetime.date(2024, 6, 17), None, "María Gómez")

# Devolvemos un libro
prestamo1.fecha_devolucion = datetime.date(2024, 6, 19)
libro1.devolver()

# Mostramos información de un libro y un préstamo
print(f"Información del libro {libro1.titulo}:")
libro1.mostrar_informacion()

print("\nInformación del préstamo:")
prestamo1.mostrar_informacion()
