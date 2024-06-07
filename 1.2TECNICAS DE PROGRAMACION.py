class Personaje:

    def __init__(self, nombre, especie, ataque, defensa, vida):
        self.nombre = nombre
        self.especie = especie
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Especie:", self.especie)
        print("·Ataque:", self.ataque)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, ataque, defensa):
        self.ataque = self.ataque + ataque
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.ataque - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):

    def __init__(self, nombre, especie, ataque, defensa, vida, armadura):
        super().__init__(nombre, especie, ataque, defensa, vida)
        self.armadura = armadura

    def cambiar_armadura(self):
        opcion = int(input("Elige una armadura: (1) Cuero, defensa 2. (2) Placa, defensa 5"))
        if opcion == 1:
            self.armadura = 2
        elif opcion == 2:
            self.armadura = 5
        else:
            print("Número de armadura incorrecta")

    def atributos(self):
        super().atributos()
        print("·Armadura:", self.armadura)

    def daño(self, enemigo):
        return self.ataque - enemigo.defensa


class Mago(Personaje):

    def __init__(self, nombre, especie, ataque, defensa, vida, hechizo):
        super().__init__(nombre, especie, ataque, defensa, vida)
        self.hechizo = hechizo

    def atributos(self):
        super().atributos()
        print("·Hechizo:", self.hechizo)

    def daño(self, enemigo):
        return self.ataque * self.hechizo - enemigo.defensa


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


personaje_1 = Guerrero("Ragnar", "Humano", 25, 15, 120, 2)
personaje_2 = Mago("Serana", "Elfo", 15, 20, 100, 4)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
