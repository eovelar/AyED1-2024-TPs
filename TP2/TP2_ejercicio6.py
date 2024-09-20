"""
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
def normalizar(lista):
    """
    Normaliza una lista de números enteros dividiendo cada elemento por la suma total de la lista

    Args:
        lista (list[int]): La lista de números enteros a normalizar

    Returns:
        list[float]: La lista normalizada

    Raises:
        ValueError: Si la suma total de la lista es cero
    """
    suma_total = sum(lista)
    if suma_total == 0:
        raise ValueError("No se puede realizar el cálculo")
    return [x / suma_total for x in lista]

def main():
    """
    Ejecuta la función principal del programa
    """
    lista_original = [1, 1, 2]
    lista_normalizada = normalizar(lista_original)
    print(f"Lista original: {lista_original}")
    print(f"Lista normalizada: {lista_normalizada}")

if __name__ == "__main__":
    main()