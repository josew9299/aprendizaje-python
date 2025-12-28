import math
import sys
from datetime import datetime
print(f"Python path: {sys.executable}")
print(f"Python version: {sys.version}")

# Ejercicios #1
#Crea una función que reciba dos parámetros #
# (un número y un exponente entero y retorne el resultado de elevar el númrto al exponente.

# Versión 1: Usando el operador ** (la forma más pythonica)
def calculate_exponent_1(num, exp):
    return num ** exp

#Manera 2: Usando la funcion pow()
def calcular_exponente(num,exp):
    pwr = pow(num,exp)
    return(pwr)
print(calcular_exponente(3,5))


#Manera 3:Usando la función math.pow()

def calculate_exponent(num, exp):
    return(math.pow(num, exp))
print(calculate_exponent(4,6))



#Manera 4: Usando un bucle for
def calcular_potencia_4(base, exponente):
    resultado = 1                   # ← 4 espacios
    for _ in range(exponente):       # ← 4 espacios
        resultado *= base           # ← 8 espacios (4 + 4)
    return resultado                 # ← 4 espacios

print(calcular_potencia_4(5,7))

#Manera 5: Usando un buclle while
def calcu_exponent(num, exp):
    i = 1
    answer = num
    while i < exp:
        answer = answer * num
        i = i + 1
    return answer

print(calcu_exponent(6,8))

#Bucle for
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

#Reto #1
#De esta manera repito una palabra n número de veces
wor_1 = input("Escribe una palabra: ")
for i in range(10) :
    print(wor_1)
else:
    print("Ok")

#Challenge #2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad).
#Preguntar la edad con un input
#Calcular el año de nacimiento
#Mostar una secuencia desde el año uno
def calcu_edad():

    now = datetime.now
    #Para preguntar la edad
    edad_1=int(input("Cual es tu edad?: "))

    if edad_1 <= 0 or edad_1 >= 120:
        print("Porfavor, ingresa una edad válida")
    
    

    #Encontrar el año de nacimiento

    anio_nac = 2025 - edad_1
    print("Usted nació entre el año ",anio_nac - 1, "y", anio_nac)

    calcu_edad()

calcu_edad()