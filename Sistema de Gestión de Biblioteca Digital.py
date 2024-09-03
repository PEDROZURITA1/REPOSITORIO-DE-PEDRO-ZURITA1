class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True  # Indica si el libro está disponible para préstamo

    def __str__(self):
        return f"{self.titulo} por {self.autor} - Categoría: {self.categoria} - ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)
        libro.disponible = False

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.disponible = True

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios = set()  # Conjunto para manejar IDs únicos de usuarios

    # Añadir un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        return f"Libro '{libro.titulo}' agregado a la biblioteca."

    # Quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            return f"Libro '{libro.titulo}' eliminado de la biblioteca."
        return "Libro no encontrado."

    # Registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in [user.id_usuario for user in self.usuarios]:
            return f"Usuario con ID '{usuario.id_usuario}' ya está registrado."
        self.usuarios.add(usuario)
        return f"Usuario '{usuario.nombre}' registrado exitosamente."

    # Dar de baja un usuario existente
    def dar_baja_usuario(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            self.usuarios.remove(usuario)
            return f"Usuario '{usuario.nombre}' dado de baja."
        return "Usuario no encontrado."

    # Prestar un libro a un usuario
    def prestar_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.libros.get(isbn, None)
        if usuario and libro and libro.disponible:
            usuario.prestar_libro(libro)
            return f"Libro '{libro.titulo}' prestado a {usuario.nombre}."
        return "Préstamo no realizado. Verifica el ID del usuario o la disponibilidad del libro."

    # Devolver un libro prestado por un usuario
    def devolver_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.libros.get(isbn, None)
        if usuario and libro:
            usuario.devolver_libro(libro)
            return f"Libro '{libro.titulo}' devuelto por {usuario.nombre}."
        return "Devolución no realizada. Verifica el ID del usuario o el ISBN del libro."

    # Buscar libros por título, autor o categoría
    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        if resultados:
            return resultados
        return "No se encontraron libros que coincidan con los criterios de búsqueda."

    # Buscar un usuario por ID
    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    # Listar libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            return usuario.libros_prestados
        return "Usuario no encontrado."

# Ejemplo de uso del sistema

# Crear algunos libros
libro1 = Libro("1984", "George Orwell", "Distopía", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "2345678901")

# Crear usuarios
usuario1 = Usuario("Pedro Zurita", "U001")
usuario2 = Usuario("María López", "U002")

# Crear la biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
print(biblioteca.agregar_libro(libro1))
print(biblioteca.agregar_libro(libro2))

# Registrar usuarios
print(biblioteca.registrar_usuario(usuario1))
print(biblioteca.registrar_usuario(usuario2))

# Prestar un libro
print(biblioteca.prestar_libro("U001", "1234567890"))

# Listar libros prestados a un usuario
libros_prestados = biblioteca.listar_libros_prestados("U001")
if isinstance(libros_prestados, list):
    for libro in libros_prestados:
        print(libro)
else:
    print(libros_prestados)

# Devolver un libro
print(biblioteca.devolver_libro("U001", "1234567890"))

# Buscar libros por autor
resultados = biblioteca.buscar_libro('autor', "George Orwell")
if isinstance(resultados, list):
    for libro in resultados:
        print(libro)
else:
    print(resultados)

# Quitar un libro de la biblioteca
print(biblioteca.quitar_libro("1234567890"))

# Dar de baja un usuario
print(biblioteca.dar_baja_usuario("U001"))
