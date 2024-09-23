"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
"""

def es_capicua(s: str) -> bool:
    """
    Verifica si una cadena es capicúa

    Args:
        s (str): La cadena a verificar

    Returns:
        bool: True si es capicúa, en caso contrario False
    """
    izquierda = 0
    derecha = len(s) - 1

    while izquierda < derecha:
        if s[izquierda] != s[derecha]:
            return False
        izquierda += 1
        derecha -= 1

    return True

def main():
    """
    Programa para probar la función es_capicua
    """
    while True:
        s = input("Ingrese una cadena: ")
        try:
            if es_capicua(s):
                print(f"'{s}' es una capicúa.")
            else:
                print(f"'{s}' no es una capicúa.")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")

        respuesta = input("¿Probar otra cadena? (s/n): ")
        if respuesta.lower() != 's':
            print("Saliendo...")
            break
            

if __name__ == "__main__":
    main()