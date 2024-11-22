"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""

def ultimos_n_caracteres(cadena, n):
    """
    Devuelve una subcadena con los últimos N caracteres de una cadena dada.

    Parámetros:
        cadena (str): La cadena original.
        n (int): El número de caracteres a devolver

    Returns:
        str: La subcadena con los últimos N caracteres
    """
    if n > len(cadena):
        return "Error: N es mayor que la longitud de la cadena"
    else:
        return cadena[-n:]

def main():
    cadena = input("Ingrese una cadena: ")
    n = int(input("Ingrese el número de caracteres a devolver: "))
    resultado = ultimos_n_caracteres(cadena, n)
    print("Los últimos", n, "caracteres de la cadena son:", resultado)

if __name__ == "__main__":
    main()
