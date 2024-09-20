"""
Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa
"""

from random import randint as rn
from typing import List

def lista_aleatoria(longitud: int) -> List[int]:
    """
    Genera una lista aleatoria de números enteros entre 1 y 100
    con la longitud especificada.
    """
    return [rn(1,100) for _ in range(longitud)]

def repetidos_lista(lista: List[int]) -> bool:
    """
    Verifica si hay elementos repetidos en la lista.

    args:
        lista (List[int]): La lista a verificar

    returns:
        bool: True si hay elementos repetidos, False en caso contrario
    """
    return len(lista) != len(set(lista))

def lista_unicos(lista: List[int]) -> List[int]:
    """
    Devuelve la lista de elementos únicos sin duplicados.
    """
    return list(set(lista))

def main():
    lista = lista_aleatoria(20)
    print("Lista original:", lista)
    """
    Verifica si hay elementos repetidos
    """
    if repetidos_lista(lista):
        print("La lista tiene elementos repetidos.")
    else:
        print("La lista no tiene elementos repetidos.")
    """
    Obtiene la lista de elementos únicos
    """
    lista_sin_duplicados = lista_unicos(lista)
    print("Lista de elementos únicos:", lista_sin_duplicados)

if __name__ == "__main__":
    main()