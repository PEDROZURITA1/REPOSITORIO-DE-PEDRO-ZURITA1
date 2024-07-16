import os

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido del archivo de código especificado.

    :param ruta_script: Ruta del archivo de script a mostrar.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def listar_scripts(ruta_base):
    """
    Lista todos los scripts disponibles en el directorio base y sus subdirectorios.

    :param ruta_base: Ruta base donde buscar los scripts.
    :return: Diccionario con las rutas de los scripts.
    """
    opciones = {}
    contador = 1
    for root, dirs, files in os.walk(ruta_base):
        for file in files:
            if file.endswith('.py'):
                ruta_relativa = os.path.relpath(os.path.join(root, file), ruta_base)
                opciones[str(contador)] = ruta_relativa
                contador += 1
    return opciones

def mostrar_menu():
    """
    Muestra el menú principal del dashboard y gestiona la interacción con el usuario.
    """
    ruta_base = os.path.dirname(__file__)

    while True:
        print("\nMenu Principal - Dashboard")
        print("1 - Listar y seleccionar scripts disponibles")
        print("2 - Agregar nueva ruta de script")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            break
        elif eleccion == '1':
            opciones = listar_scripts(ruta_base)
            if opciones:
                for key in opciones:
                    print(f"{key} - {opciones[key]}")
                eleccion_script = input("Elige un script para ver su código o '0' para volver al menú: ")
                if eleccion_script in opciones:
                    mostrar_codigo(os.path.join(ruta_base, opciones[eleccion_script]))
                elif eleccion_script != '0':
                    print("Opción no válida. Por favor, intenta de nuevo.")
            else:
                print("No se encontraron scripts disponibles.")
        elif eleccion == '2':
            nueva_ruta = input("Introduce la ruta del nuevo script: ")
            if os.path.isfile(nueva_ruta):
                with open("rutas_scripts.txt", "a") as file:
                    file.write(f"{nueva_ruta}\n")
                print("Ruta agregada con éxito.")
            else:
                print("La ruta no es válida o el archivo no existe.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
