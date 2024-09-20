"""
Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado. 
"""
pacientes = []
urgencia = []

def clinica():
    """
    Función para cargar pacientes y sus respectivos tipos de atención (urgencia o turno)
    
    Pide al usuario que ingrese los datos de los pacientes y los almacena en las listas pacientes y urgencia
    """
    ingreso = ""
    while ingreso != "-1":
        ingreso = input("Ingrese numero de afiliado (-1 para finalizar la carga): ")
        if ingreso == "-1":
            break
        urgente = input("Indique si viene por urgencia (0) o con turno (1): ")
        if len(ingreso) < 4 or len(ingreso) > 4:
            print("Numero de afiliado incorrecto")
            continue
        elif urgente != "0" and urgente != "1":
            print("Ingrede un valor entre 0 o 1")
            continue
        else:
            pacientes.append(ingreso)
            urgencia.append(urgente)

def mostrar_pacientes():
    """
    Función para mostrar pacientes urgentes y pacientes con turno.
    
    Retorna dos listas: una con pacientes urgentes y otra con pacientes con turno
    """
    p_urgencia = [pacientes[i] for i in range(len(pacientes)) if urgencia[i] == "0"]
    p_turno = [pacientes[i] for i in range(len(pacientes)) if urgencia[i] == "1"]
    return p_urgencia, p_turno

def veces_atendido():
    """
    Función para mostrar cuántas veces ha sido atendido un paciente por urgencia o turno
    
    Pide al usuario que ingrese el número de afiliado y muestra el número de veces que ha sido atendido
    """
    afiliado = ""
    while afiliado != "-1":
        afiliado = input("Ingrese el numero de afiliado: ")
        if afiliado == "-1":
            break
        if afiliado in pacientes:
            turno = 0
            urg = 0
            for i in range(len(pacientes)):
                if pacientes[i] == afiliado:
                    if urgencia[i] == "1":
                        turno += 1
                    else:
                        urg += 1
            print(f"Afiliado {afiliado}: Atendido por turno: {turno}, Atendido por urgencia: {urg}")
        else:
            print("Número de afiliado no encontrado.")

"""
Llamada a la función clinica()
"""
clinica()

"""
Llamada a la función mostrar_pacientes()
"""
p_urgencia, p_turno = mostrar_pacientes()
print("Pacientes urgentes:", p_urgencia)
print("Pacientes con turno:", p_turno)

veces_atendido()