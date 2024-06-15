class Dia:
    """
    Clase que representa la información de un día específico.

    Atributos:
        fecha (str): La fecha del día (formato dd/mm/aaaa).
        temperatura (float): La temperatura del día.
    """

    def __init__(self, fecha, temperatura):
        """
        Constructor de la clase Dia.

        Parámetros:
            fecha (str): La fecha del día.
            temperatura (float): La temperatura del día.
        """
        self.fecha = fecha
        self.temperatura = temperatura

    def mostrar(self):
        """
        Muestra la información del día (fecha y temperatura) en formato legible.
        """
        print(f"Fecha: {self.fecha}, Temperatura: {self.temperatura:.2f}")


class Semana:
    """
    Clase que representa una semana y gestiona la información de los días.

    Atributos:
        dias (list): Una lista que contiene instancias de la clase Dia (representando los días de la semana).
    """

    def __init__(self):
        """
        Constructor de la clase Semana.
        Inicializa la lista de días vacía.
        """
        self.dias = []

    def agregar_dia(self, dia):
        """
        Agrega un día (instancia de la clase Dia) a la lista de días de la semana.

        Parámetros:
            dia (Dia): La instancia de la clase Dia que representa el día a agregar.
        """
        self.dias.append(dia)

    def calcular_promedio(self):
        """
        Calcula el promedio semanal de las temperaturas de los días registrados.

        Retorna:
            float: El promedio semanal de las temperaturas.
        
        Excepciones:
            Exception: Si no hay días registrados en la semana, se lanza una excepción.
        """
        if not self.dias:
            raise Exception("No hay días registrados en la semana")

        temperaturas = [dia.temperatura for dia in self.dias]
        promedio = sum(temperaturas) / len(temperaturas)
        return promedio

    def mostrar_promedio(self):
        """
        Muestra el promedio semanal de la temperatura al usuario.
        """
        try:
            promedio = self.calcular_promedio()
            print
