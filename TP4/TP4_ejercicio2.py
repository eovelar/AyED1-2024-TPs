"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
"""
def imprimir_centralizado(cadena: str) -> None:
    """
    Calcula el número de espacios necesarios para centrar la cadena
    """
    espacios = (80 - len(cadena)) // 2
    print(" " * espacios + cadena)

def main() -> None:
    """
    Lee una cadena de caracteres del usuario y la imprime centrada en pantalla
    """
    cadena = input("Ingrese una cadena: ")
    imprimir_centralizado(cadena)

if __name__ == "__main__":
    main()