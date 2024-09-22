"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla.
"""
import random
from typing import List

def crear_matriz_aleatoria(n: int) -> List[List[int]]:
    """
    Crea una matriz de N x N con números enteros al azar sin repetir ninguno
    """
    numeros = list(range(n**2))  
    random.shuffle(numeros) 
    matriz = [numeros[i*n:(i+1)*n] for i in range(n)] 
    return matriz

def imprimir_matriz(matriz: List[List[int]]) -> None:
    """
    imprime la matriz por pantalla
    """
    for fila in matriz:
        print(fila)

def main():
    n = int(input("Ingrese el valor de N: "))
    matriz = crear_matriz_aleatoria(n)
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()