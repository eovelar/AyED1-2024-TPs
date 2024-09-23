"""
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función.
"""
def ordenada(lista):
    """
    Verifica si una lista está ordenada en forma ascendente

    """
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))

def main():
    lista = input("Ingrese la lista (separada por comas): ")
    lista = [x.strip() for x in lista.split(",")]
    
    try:
        lista = [int(x) for x in lista]
    except ValueError:
        pass
    
    print("La lista es:", lista)
    print("La lista está ordenada:", ordenada(lista))

if __name__ == "__main__":
    main()