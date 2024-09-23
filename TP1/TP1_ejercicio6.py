"""
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
def normalizar(lista):
    """
    Normaliza una lista de números enteros, de manera que todos sus elementos sumen 1.0,
    respetando las proporciones relativas que cada elemento tiene en la lista original
    
    """
    suma_total = sum(lista)
    return [elemento / suma_total for elemento in lista]

def main():
    lista = input("Ingrese la lista de números enteros (separada por comas): ")
    lista = [int(x) for x in lista.split(",")]
    
    print("La lista original es:", lista)
    print("La lista normalizada es:", normalizar(lista))

if __name__ == "__main__":
    main()