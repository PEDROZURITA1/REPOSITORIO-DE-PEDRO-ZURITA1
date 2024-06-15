def obtener_numero_de_dias():
    """
    Solicita al usuario el número de días de la semana y lo devuelve como un entero.

    Retorna:
        int: El número de días ingresado por el usuario.
    """
    numero_de_dias = int(input("Ingrese el número de días de la semana: "))
    return numero_de_dias


def obtener_temperaturas(numero_de_dias):
    """
    Solicita al usuario las temperaturas para cada día de la semana y las almacena en una lista.

    Parámetros:
        numero_de_dias (int): El número de días de la semana.

    Retorna:
        list: Una lista que contiene las temperaturas ingresadas por el usuario.
    """
    temperaturas = []
    for _ in range(numero_de_dias):
        temperatura = float(input(f"Ingrese la temperatura para el día {_+1}: "))
        temperaturas.append(temperatura)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal de las temperaturas almacenadas en una lista.

    Parámetros:
        temperaturas (list): La lista de temperaturas.

    Retorna:
        float: El promedio semanal de las temperaturas.
    """
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


def mostrar_promedio(promedio):
    """
    Muestra el promedio semanal de la temperatura al usuario.

    Parámetros:
        promedio (float): El promedio semanal de las temperaturas.
    """
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}")


def main():
    """
    Función principal que controla el flujo del programa.
    """
    numero_de_dias = obtener_numero_de_dias()
    temperaturas = obtener_temperaturas(numero_de_dias)
    promedio = calcular_promedio(temperaturas)
    mostrar_promedio(promedio)


if __name__ == "__main__":
    main()
