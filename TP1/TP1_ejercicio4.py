"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""
def eliminar_valores(lista_original, lista_eliminar):
    """
    Elimina los valores de la lista_original que se encuentran en la lista_eliminar
    """
    for valor in lista_eliminar:
        while valor in lista_original:
            lista_original.remove(valor)

def main():
    lista_original = input("Ingrese la lista original (separada por comas): ")
    lista_original = [int(x) for x in lista_original.split(",")]
    
    lista_eliminar = input("Ingrese la lista de valores a eliminar (separada por comas): ")
    lista_eliminar = [int(x) for x in lista_eliminar.split(",")]
    
    print("Lista original:", lista_original)
    print("Lista de valores a eliminar:", lista_eliminar)

    eliminar_valores(lista_original, lista_eliminar)

    print("Lista resultante:", lista_original)

if __name__ == "__main__":
    main()