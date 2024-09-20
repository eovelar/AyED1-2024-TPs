"""
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
"""
def lista_impares():
    """
    Genera una lista de números impares desde 100 hasta 200
    """
    return [n for n in range(100, 201) if n % 2 != 0]