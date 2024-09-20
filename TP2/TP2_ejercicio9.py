"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""
def lista_multiplos_siete():
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))
    return [n for n in range(a, b+1) if n % 7 == 0 and n % 5 != 0]

print("Lista de múltiplos de 7 que no son múltiplos de 5:")
print(lista_multiplos_siete())