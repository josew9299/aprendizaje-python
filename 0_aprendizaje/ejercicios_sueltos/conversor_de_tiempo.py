from operator import truediv
from queue import Empty


MINUTO = 60
HORA = 3600
DIA = 86400
CONTINUAR = True
operacion = input("Ingresa la conversión que quieras hacer: ")
entrada = float(input("Ingresa el timepo en números: "))

"""

Este es un conversor inicial de
tiempo que puedes utilizar para
convertir de horas a minutos,minutos a
segundos, horas a segundos y viceversa.
"""


def convertidor_minutos():
    
    """
    Esta función convierte minutos a 
    segundos, minutos a horas y 
    minutos a días.
    """
    minutos = operacion
    if minutos == "m-s": #Minutos a segundos
        return entrada * MINUTO
    
    elif minutos == "m-h":#minutos a horas
        return ((entrada * MINUTO ) * 24)
    
    elif minutos == "m-d": #minutos a días
        return (entrada / DIA) * MINUTO
    else:
        return("Error!")



def convertidor_segundos():
    """
    Esta función convierte segundos a minutos,
    segundos a horas y segundoa a días.
    """
    segundos = operacion
    time_0 = entrada
    
    if segundos == "s-m":# segundos a minutos
        return time_0 / MINUTO
    
    elif segundos == "s-h":#segundos a horas
        return time_0 / HORA
    
    elif segundos == "s-d": #segundos a dìas
        return(time_0/DIA)
    
    else:
        return("Error!")


def convertidor_dias():
    """
    Esta función convierte días a segundos,
    días a minuto y días a horas.
    """
    dias = operacion
    time_1 = entrada
    if dias == "d-s":#dias a segundos
        return time_1 * DIA
    
    elif dias == "d-m":#días a minutos
        return (time_1 / MINUTO) * DIA
    
    elif dias == "d-h": #dìas a horas
        return (((time_1 * DIA)/HORA))
    
    else:
        return("Error!")

def convertidor_horas():
    """
    Esta función convierte horas a segundos,
    horas a minutos y horas a días.
    """
    horas = operacion
    time_2 = entrada
    if horas == "h-s":#horas a segundos
        return time_2 * HORA
    
    elif horas == "h-m":#horas a minutos
        return ((time_2 * HORA) / MINUTO)
    
    elif horas == "h-d": #horas a dìas
        return (time_2 * HORA) / DIA
    
    else:
        return("Error!")



if "h" in operacion and entrada  is True:
    convertidor_horas()
else:
    print("Error de operación")

while CONTINUAR:
    
    respuesta = input("Deseas hacer otra conversión?: Sí/No (s/n): ").strip().lower()
    
    if respuesta == "n":
        print("Muchas gracias, hasta luego!")
        CONTINUAR = False
    if respuesta == "s":
        operacion = input("Ingresa la conversión que quieras hacer: ")
        entrada = float(input("Ingresa el timepo en números: "))
        
        
    if "m-s" in operacion or "m-h" in operacion or "m-d" in operacion:

        resultado = convertidor_minutos()
        print(resultado)
        break
    elif "s-m" in operacion or "s-h" in operacion or "s-d" in operacion:
        resultado = convertidor_segundos()
        print(resultado)
        break
    
    elif "d-s" in operacion or "d-m" in operacion or "d-h" in operacion:
        resultado = convertidor_dias()
        print(resultado)
        break
    elif "h-s" in operacion or "h-m" in operacion or "h-d" in operacion:
        resultado = convertidor_horas()
        print(resultado)
        break
    else:
        print("Opción no válida. Use `s` o `n`")