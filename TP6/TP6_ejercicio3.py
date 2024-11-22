"""
3. Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo.

"""

import os

def GrabarRangoAlturas(nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        while True:
            deporte = input("Ingrese el nombre del deporte (o 'fin' para terminar): ")
            if deporte.lower() == 'fin':
                break
            
            archivo.write(f"{deporte}\n")
            while True:
                altura = input(f"Ingrese la altura del atleta (o 'fin' para terminar): ")
                if altura.lower() == 'fin':
                    break
                archivo.write(f"{altura}\n")

def GrabarPromedio(nombre_archivo_alturas, nombre_archivo_promedios):
    promedios = {}
    
    with open(nombre_archivo_alturas, 'r', encoding='utf-8') as archivo:
        deporte_actual = None
        alturas = []

        for linea in archivo:
            linea = linea.strip()
            if linea: 
                if linea.isalpha(): 
                    if deporte_actual and alturas:
                        promedio = sum(alturas) / len(alturas)
                        promedios[deporte_actual] = promedio
                    deporte_actual = linea
                    alturas = []
                else:  
                    try:
                        altura = float(linea)
                        alturas.append(altura)
                    except ValueError:
                        print(f"Error: '{linea}' no es una altura válida.")
        

        if deporte_actual and alturas:
            promedio = sum(alturas) / len(alturas)
            promedios[deporte_actual] = promedio


    with open(nombre_archivo_promedios, 'w', encoding='utf-8') as archivo:
        for deporte, promedio in promedios.items():
            archivo.write(f"{deporte}\n")
            archivo.write(f"{promedio}\n")

def MostrarMasAltos(nombre_archivo_promedios):
    promedios = {}
    total_alturas = 0
    total_deportes = 0

    with open(nombre_archivo_promedios, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea: 
                if linea.isalpha():  
                    deporte_actual = linea
                else:  
                    try:
                        promedio = float(linea)
                        promedios[deporte_actual] = promedio
                        total_alturas += promedio
                        total_deportes += 1
                    except ValueError:
                        print(f"Error: '{linea}' no es un promedio válido.")

    if total_deportes > 0:
        promedio_general = total_alturas / total_deportes
        print(f"Promedio general de alturas: {promedio_general:.2f}")
        print("Disciplinas cuyos atletas superan la estatura promedio general:")
        for deporte, promedio in promedios.items():
            if promedio > promedio_general:
                print(deporte)
    else:
        print("No se encontraron disciplinas.")

if __name__ == "__main__":
    nombre_archivo_alturas = "alturas_atletas.txt"
    nombre_archivo_promedios = "promedios_alturas.txt"
    
    GrabarRangoAlturas(nombre_archivo_alturas)
    GrabarPromedio(nombre_archivo_alturas, nombre_archivo_promedios)
    MostrarMasAltos(nombre_archivo_promedios)