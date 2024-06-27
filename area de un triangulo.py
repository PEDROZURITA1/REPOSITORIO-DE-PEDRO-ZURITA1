# Este programa calcula el area de un triangulo.

def calcular_area_triangulo(base: float, altura: float) -> float:
    """Calcula el area de un triangulo dados su base y altura.

    Args:
        base (float): La longitud de la base del triángulo.
        altura (float): La longitud de la altura del triángulo.

    Returns:
        float: El area del triangulo.
    """
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser números positivos.")

    area = (base * altura) / 2
    return area

if __name__ == "__main__":
    try:
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))

        area = calcular_area_triangulo(base, altura)
        print(f"El area del triangulo es: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
