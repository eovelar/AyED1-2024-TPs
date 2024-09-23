"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

def extraer_subcadena_a(cadena, posicion, cantidad):
    """
    Extrae una subcadena de una cadena de caracteres utilizando rebanadas

    Args:
        cadena (str): La cadena de caracteres original
        posicion (int): La posición inicial de la subcadena
        cantidad (int): La cantidad de caracteres 

    Returns:
        str: La subcadena extraída

    """
    return cadena[posicion:posicion + cantidad]

def extraer_subcadena_b(cadena, posicion, cantidad):
    """
    Extrae una subcadena de una cadena de caracteres sin utilizar rebanadas

    Args:
        cadena (str): La cadena de caracteres original
        posicion (int): La posición inicial de la subcadena
        cantidad (int): La cantidad de caracteres

    Returns:
        str: La subcadena extraída

    """
    subcadena = ""
    for i in range(posicion, posicion + cantidad):
        subcadena += cadena[i]
    return subcadena

def main():
    """
    Función principal
    """
    cadena = "El número de teléfono es 4356-7890"
    posicion = 25
    cantidad = 9

    print("Cadena original:", cadena)
    print("Posición:", posicion)
    print("Cantidad de caracteres:", cantidad)

    print("\na. Utilizando rebanadas:")
    print(extraer_subcadena_a(cadena, posicion, cantidad))

    print("\nb. Sin utilizar rebanadas:")
    print(extraer_subcadena_b(cadena, posicion, cantidad))

if __name__ == "__main__":
    main()

