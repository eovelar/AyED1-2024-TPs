"""
5. Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función. 
"""
def ordenada(lista):
    """
    Verifica si una lista está ordenada en forma ascendente.
    """
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

def main():
    """
    Función principal para probar la función 'ordenada'.
    
    Imprime los resultados de varias pruebas de la función 'ordenada'
    con diferentes tipos de listas para verificar su comportamiento
    """
    print(ordenada([1, 2, 3]))
    print(ordenada(['b', 'a']))
    print(ordenada([1, 2, 2, 3, 4]))
    print(ordenada([5, 4, 3, 2, 1]))

if __name__ == "__main__":
    main()