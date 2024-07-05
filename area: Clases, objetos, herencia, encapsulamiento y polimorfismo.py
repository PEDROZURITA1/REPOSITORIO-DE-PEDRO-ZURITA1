# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad      # Atributo encapsulado

    def hacer_sonido(self):
        return "Sonido de animal"

    def info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"


# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    # Sobrescritura de método (polimorfismo)
    def hacer_sonido(self):
        return "Guau guau"

    def info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Raza: {self.raza}"


# Clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Sobrescritura de método (polimorfismo)
    def hacer_sonido(self):
        return "Miau miau"

    def info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Color: {self.color}"


# Función principal para demostrar la funcionalidad
def main():
    # Creación de instancias
    animal = Animal("Animal Genérico", 5)
    perro = Perro("Rex", 3, "Labrador")
    gato = Gato("Misi", 2, "Blanco")

    # Demostración de encapsulación e información de las instancias
    print(animal.info())
    print(perro.info())
    print(gato.info())

    # Demostración de polimorfismo
    for animal in (animal, perro, gato):
        print(f"{animal._nombre} dice: {animal.hacer_sonido()}")


if __name__ == "__main__":
    main()
