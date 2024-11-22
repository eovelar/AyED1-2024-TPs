"""
2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""

def sumar_numeros (cadena1: str, cadena2: str) -> float:
    """
    Suma dos números reales representados como cadenas de caracteres.

    Args:
        cadena1 (str): Primera cadena que representa un número real.
        cadena2 (str): Segunda cadena que representa un número real.

    Returns:
        float: La suma de los dos números reales, o -1 si alguna cadena no es válida.
    """
    try:
        num1 = float(cadena1)
        num2 = float(cadena2)
        
        return num1 + num2
    
    except ValueError:
        return -1

if __name__ == "__main__":

    cadena1 = input("Ingrese el primer número: ")
    cadena2 = input("Ingrese el segundo número: ")
    resultado = sumar_numeros(cadena1, cadena2)

    if resultado != -1:
        print(f"La suma de los números es: {resultado}")
    else:
        print("Una de las cadenas no contiene un número válido.")