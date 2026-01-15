def mayor_edad(edad):
    if edad >=18 and edad < 120:
        return True, "Eres mayor de edad"
    if edad < 18 and edad > 0:
        return False, "Eres menor de edad"
    if edad > 120 and edad > 0:
        return False, "Es imposible vivir tanto"
    if edad < 0:
        return False, "Aún ho ha nacido o solo tiene meses de edad"
    else:
        return False, "Por favor introduce una edad válida"
    


#La serie de fibonacci


""""
Imprime este patrón por pantalla
1
2 2
3 3 3 
4 4 4 4
5 5 5 5 5
"""

for num in range(6):#Filas
    for i in range(num): #Columnas
        print(num, end=" ")
    print()