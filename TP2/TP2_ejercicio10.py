"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla. 
"""
from random import randint as rn

def lista_aleatoria():
    return [rn(1,100) for _ in range(15)]
def impares(num):
    return num % 2 != 0

numeros_aleatorios = lista_aleatoria()
numeros_impares = list(filter(impares, numeros_aleatorios))
print(numeros_impares, numeros_aleatorios)