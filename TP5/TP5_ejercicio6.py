"""
6. El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

def ingresar_numeros() -> list:
    lista_numeros = []
    while True:
        try:
            num = int(input("Ingrese los números enteros (-1 para terminar): "))
            if num == -1:
                break
            lista_numeros.append(num)
        except ValueError:
            print("Solo debe ingresar números enteros.")
    return lista_numeros

def buscar_indice(lista):
    errores = 0
    while errores < 3:
        try:
            num = int(input("Ingrese el número para sacar su índice: "))
            print(f"El número {num} está en el índice {lista.index(num)}.")
            errores = 0  
        except ValueError:
            errores += 1
            print(f"El número {num} no está en la lista. Intentos fallidos: {errores}.")
        except Exception as e:
            errores += 1
            print(f"Error: {e}. Intentos fallidos: {errores}.")
    
    print("Se alcanzó el límite de 3 errores. Saliendo del programa...")

def flujo_principal() -> None:
    """Flujo principal que maneja todo el programa.
        Returns: None
    """
    lista = ingresar_numeros()
    print("Lista ingresada:", lista)
    buscar_indice(lista)

if __name__ == "__main__":
    flujo_principal()