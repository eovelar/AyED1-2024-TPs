"""
3. Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""
def procesar_email(email):
    """
    Procesa una dirección de correo y devuelve sus partes en una tupla
    """
    if "@" not in email or email.count("@") != 1:
        return ()
    
    usuario, dominio = email.split("@")
    
    if "." not in dominio:
        return ()
    
    partes_dominio = dominio.split(".")
    
    """
    Verificar que haya al menos dos partes en el dominio (ej. uade.edu.ar)
    """
    if len(partes_dominio) < 2:
        return ()
    
    return (usuario,) + tuple(partes_dominio)

if __name__ == "__main__":
    email = input("Ingrese una dirección de correo electrónico: ")
    
    partes = procesar_email(email)
    
    if partes:
        print("Las partes de la dirección de correo electrónico son:", partes)
    else:
        print("La dirección de correo electrónico es inválida.")