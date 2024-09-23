"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna representa el día de la semana y cada fila a una de sus fábricas.

Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una
semana, considerando que la capacidad máxima de fabricación es de 150
unidades por día y puede suceder que en ciertos días no se fabrique ninguna.
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada
por cada fábrica.
"""
import random as rn

def generar_matriz(n):
    """
    Genera una matriz con datos aleatorios para N fábricas durante una semana
    """
    matriz = [[rn.randint(0, 150) for _ in range(6)] for _ in range(n)]
    return matriz

def produccion_fabrica(matriz):
    """
    Muestra la cantidad total de bicicletas fabricadas por cada una
    """
    for i, fila in enumerate(matriz):
        produccion_total = sum(fila)
        print(f"Fábrica {i+1}: {produccion_total} bicicletas")

def mayor_produccion(matriz):
    """
    Encuentra la fábrica que más produjo en un solo día
    """
    max_produccion = 0
    fabrica_max = 0
    dia_max = 0
    for i, fila in enumerate(matriz):
        for j, produccion in enumerate(fila):
            if produccion > max_produccion:
                max_produccion = produccion
                fabrica_max = i+1
                dia_max = j+1
    print(f"Fábrica {fabrica_max} produjo {max_produccion} bicicletas el día {dia_max}")

def dia_mas_productivo(matriz):
    """
    Encuentra el día más productivo de todas las fábricas en total
    """
    produccion_por_dia = [sum(fila[i] for fila in matriz) for i in range(6)]
    max_produccion = max(produccion_por_dia)
    dia_max = produccion_por_dia.index(max_produccion) + 1
    print(f"El día {dia_max} fue el más productivo con {max_produccion} bicicletas")

def menor_produccion(matriz):
    """
    Devuelve una lista por comprensión que contiene la menor producción por cada fábrica
    """
    menor_produccion_por_fabrica = [min(fila) for fila in matriz]
    print("Menor cantidad fabricada por cada fábrica:")
    for i, produccion in enumerate(menor_produccion_por_fabrica):
        print(f"Fábrica {i+1}: {produccion} bicicletas")

def main():
    """
    Función principal para ejecutar el programa
    """
    n = int(input("Ingrese el número de fábricas: "))
    matriz = generar_matriz(n)

    print("Matriz de producción:")
    for fila in matriz:
        print(fila)

    produccion_fabrica(matriz)
    mayor_produccion(matriz)
    dia_mas_productivo(matriz)
    menor_produccion(matriz)

if __name__ == "__main__":
    main()