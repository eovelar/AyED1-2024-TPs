"""
1. Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""

def num_natural() -> int:
    """
    Solicita al usuario que ingrese un número natural (mayor que 0) y valida la entrada.
    La función maneja excepciones para asegurar que la entrada sea un número entero
    """

    while True:
        try:
            entrada = input("Ingrese un número: ")
            numero = int(entrada)
            
            if numero <= 0:
                raise ValueError("El número debe ser mayor que 0.")
            
            return numero
        
        except ValueError as e:
            print(f"Error: {e}. Entrada no válida, ingrese únicamente un número entero positivo.")

if __name__ == "__main__":
    while True:
        num = num_natural()
        if num:
            print(num)
        else:
            print("Entrada no válida")
