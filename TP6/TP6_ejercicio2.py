"""
2. Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.

"""
import os

import os

def dividir_archivo(ruta_archivo, tamanio_maximo):
    """Divide un archivo en partes de tamaño máximo especificado
    """
    try:
        if not os.path.isfile(ruta_archivo):
            print("Error: El archivo no existe.")
            return
        
        parte_numero = 1
        tamanio_actual = 0
        nombre_base, extension = os.path.splitext(ruta_archivo)
        archivo_salida = None

        with open(ruta_archivo, "rt", encoding="utf-8") as archivo:
            for linea in archivo:
                tamanio_actual += len(linea.encode('utf-8')) 

                if tamanio_actual > tamanio_maximo:
                    if archivo_salida:
                        archivo_salida.close()
                    parte_numero += 1
                    tamanio_actual = len(linea.encode('utf-8')) 
                    archivo_salida = open(f"{nombre_base}_parte{parte_numero}{extension}", "wt", encoding="utf-8")

                if archivo_salida:
                    archivo_salida.write(linea)

            if archivo_salida:
                archivo_salida.close()

        print("División completada.")

    except ValueError:
        print("Error: El tamaño máximo debe ser un número entero.")

if __name__ == "__main__":
    ruta_archivo = input("Ingrese el nombre del archivo a dividir: ")
    
    try:
        tamanio_maximo = int(input("Ingrese el tamaño de cada parte: "))
        dividir_archivo(ruta_archivo, tamanio_maximo)
    except ValueError:
        print("Error: El tamaño máximo debe ser un número entero.")