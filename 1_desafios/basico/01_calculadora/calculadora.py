"""Esta es una calculadora básica con los bucles for y while
#Problemas
#1. Necesito dos entradas
#2. Hacer la operación matemática y evaluarala.
#3. Que contenga las 4 operaciones matemáticas básicas
#4. Mostrar el resultado.
#5. Que no se cierre hasta darle la orden de salir
"""
cal = "Bienvenido a la calculadora de\n operacioens matemáticas básicas"
print (cal)
def calculadora_00():
    """Calcula"""
    try:
        #Entrada
        n1 = float(input("Introduzca su primer número: "))
        sign = input("Indique la operación a realizar\n+ Suma\n- resta/substracción\n* Multiplicación  \n^^ Potenciación\n / división\n: ")
        n2 = float(input("Ingrese su segundo número: "))
    except:
        print("Error")
        calculadora_00()

    #Operaciones
    def sum_two(n1,n2):
        #"""Suma dos números tipo float"""
        return n1+n2

    def multiply_two(n1,n2):
        #"""Multiplica dos números tipo float""" 
        return n1*n2

    def divide_two(n1,n2):
        #"""Divide dos números tipo float""" 
        return n1/n2

    def subs_two(n1,n2):
        #"""Resta un valor  del otro, siendo ambos de tipo float"""
        return n1-n2

    def power(n1,n2):
        #"""Calcula la potencia de un número"""
        return n1**n2


    #Evaluación de las operaciones

    try:
        if n1 == n1 and sign == "+" and n2 == n2:
            #"""Evalúa la operación sumar"""
            sum_two(n1,n2)
            print("El resultado es: ",sum_two(n1,n2))
            print("")
            print("")

        elif n1 == n1 and sign == "-" and n2== n2:
            #"""Evalúa la operación restar"""
            subs_two(n1,n2)
            print("El resultado es: ",subs_two(n1,n2))
            print("")
            print("")

        elif n1 == n1 and sign == "*" and n2 == n2 :
            #"""Evalúa la operación multiplicar"""
            multiply_two(n1,n2)
            print("El resultado es: ",multiply_two(n1,n2))
            print("")
            print("")

        elif n1 == n1 and sign == "/" and n2==n2:
            #"""Evalúa la operación dividir"""
            divide_two(n1,n2)
            print("El resultado es: ",divide_two(n1,n2))
            print("")
            print("")

        elif n1 == n1 and sign == "^^" and n2 == n2:
            #"""Evalúa la operación potenciar"""
            power(n1,n2)
            print("El resultado es:", power(n1,n2))
            print("")
            print("") 

        else:
            print("Error")
    except:
        calculadora_00()



while True:
    calculadora_00()