"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""
from random import randint as rn
from typing import List

def lista_aleatoria() -> List[int]:
    """
    Devuelve una lista de números enteros aleatorios entre 1000 y 9999.
    La longitud de la lista también es aleatoria, entre 10 y 99.
    """
    return [rn(1000, 9999) for _ in range(rn(10, 99))]

def producto_lista(lista: List[int]) -> int:
    """
    Devuelve el producto de todos los elementos de la lista.
    Precondición: lista no está vacía.
    """
    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_elemento(num: int, lista: List[int]) -> None:
    """
    Elimina todas las ocurrencias de num de lista.
    Precondición: num es un número entero, lista es una lista de números enteros.
    Postcondición: num no está en lista.
    """
    while num in lista:
        lista.remove(num)

def es_capicua(lista: List[int]) -> bool:
    """
    Devuelve True si lista es un palíndromo, False en caso contrario.
    """
    return lista == lista[::-1]

def main():
    lista = lista_aleatoria()
    print("Lista original:", lista)
    print("El producto de la lista es", producto_lista(lista))
    num_eliminar = lista[0]
    eliminar_elemento(num_eliminar, lista)
    print("Lista después de eliminar", num_eliminar, ":", lista)
    print("Es capicúa:", es_capicua(lista))

if __name__ == "__main__":
    main()