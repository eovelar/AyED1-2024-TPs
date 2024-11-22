"""
8. Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""
def main():
    numeros = set(range(10))
    
    print("Conjunto inicial:", numeros)
    
    while True:
        try:
            valor = int(input("Ingrese un número para eliminar del conjunto (ingrese -1 para finalizar): "))

        
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