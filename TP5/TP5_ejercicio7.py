"""
Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más.
"""
import random as rn

def adivinar_num():
    numero_secreto = rn.randint(1, 500)
    intentos = 0 

    while True:
        entrada = input("Adivina el número entre 1 y 500 (-1 para salir del juego): ")
        intentos += 1  

        try:
            adivinanza = int(entrada) 

            if adivinanza < numero_secreto:
                print("El número a adivinar es mayor.")
            elif adivinanza > numero_secreto:
                print("El número a adivinar es menor.")
            else:
                print(f"Felicitaciones!! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break  

        except ValueError:
            print("El número ingresado no es válido. Intente nuevamente")

if __name__ == "__main__":
    adivinar_num()