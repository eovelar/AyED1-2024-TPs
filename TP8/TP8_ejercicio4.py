"""
4. Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""
def fichas_encajan(ficha1, ficha2):
    """Verifica si dos fichas de dominó encajan."""
    conjunto_ficha1 = set(ficha1)
    conjunto_ficha2 = set(ficha2)
    
    return not conjunto_ficha1.isdisjoint(conjunto_ficha2)

if __name__ == "__main__":
    ficha1 = tuple(map(int, input("Ingrese la primera ficha (formato: a,b): ").split(',')))
    ficha2 = tuple(map(int, input("Ingrese la segunda ficha (formato: a,b): ").split(',')))
    
    if fichas_encajan(ficha1, ficha2):
        print(f"Las fichas {ficha1} y {ficha2} encajan.")
    else:
        print(f"Las fichas {ficha1} y {ficha2} no encajan.")