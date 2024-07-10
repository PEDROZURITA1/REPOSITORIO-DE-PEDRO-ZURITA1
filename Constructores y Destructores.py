class Animal:
    def __init__(self, nombre, edad):
        # Constructor: Se llama cuando se crea un nuevo objeto de esta clase
        self.nombre = nombre
        self.edad = edad
        print(f"Animal creado: {self.nombre}, {self.edad} años")

    def __del__(self):
        # Destructor: Se llama cuando el objeto es destruido
        print(f"Animal destruido: {self.nombre}")

    def describir(self):
        print(f"Soy un animal llamado {self.nombre} y tengo {self.edad} años")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamada al constructor de la clase padre (Animal)
        super().__init__(nombre, edad)
        self.raza = raza
        print(f"Perro de raza {self.raza} creado")

    def __del__(self):
        # Llamada al destructor de la clase padre (Animal)
        super().__del__()
        print(f"Perro de raza {self.raza} destruido")

    def describir(self):
        # Sobrescribiendo el método describir
        super().describir()
        print(f"También soy un perro de la raza {self.raza}")


# Creación de objetos para demostrar el uso de constructores y destructores
def main():
    print("Inicio del programa")
    # Creando un objeto de la clase Animal
    animal1 = Animal("Lola", 5)
    animal1.describir()

    # Creando un objeto de la clase Perro (hereda de Animal)
    perro1 = Perro("Firulais", 3, "Labrador")
    perro1.describir()

    # Eliminando objetos explícitamente
    del animal1
    del perro1
    print("Fin del programa")


if __name__ == "__main__":
    main()
