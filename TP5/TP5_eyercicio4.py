"""
4. Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""
def imprimir_num():
    """
    Esta función imprime los números dentro del rango 1 al 100.000 hasta que el usuario interrumpa
    el programa mediante Ctrl-C, o en su defecto termine de imprimirlos.

    """
    try:
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        confirm = input("\n¿Desea detener el programa? (s/n): ")
        if confirm.lower() == 's':
            print("Programa detenido. Saliendo...")
        else:
            imprimir_num()

if __name__ == "__main__":
    imprimir_num()