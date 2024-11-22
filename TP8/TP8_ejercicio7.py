"""
8.Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.

"""
def main():
    """
    Definir el conjunto con números enteros entre 0 y 9
    """
    numeros = set(range(10))
    
    print("Conjunto inicial:", numeros)
    
    while True:
        try:
            valor = int(input("Ingrese un número para eliminar del conjunto (-1 para finalizar): "))
            
            if valor == -1:
                print("Proceso finalizado.")
                break
            
            numeros.remove(valor)
            print(f"Número {valor} eliminado. Conjunto actual: {numeros}")
        
        except KeyError:
            print(f"El número {valor} no está en el conjunto.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()