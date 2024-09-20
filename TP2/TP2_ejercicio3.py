"""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 
"""
import random as rn

def lista_cuadrados(n: int) -> list:
    """
    Devuelve una lista de cuadrados de números enteros desde 1 hasta n
    """
    return [i**2 for i in range(1, n+1)]

def mostrar_ultimos_diez(lista: list) -> None:
    """
    Muestra los últimos 10 elementos de una lista.

    Args:
        lista (list): La lista que se quiere mostrar

    Returns:
        None
    """
    for valor in lista[-10:]:
        print(valor)

n = int(input("Ingrese un número: "))

"""
Genera la lista de cuadrados
"""
lista_cuadrados_prueba = lista_cuadrados(n)
mostrar_ultimos_diez(lista_cuadrados_prueba)