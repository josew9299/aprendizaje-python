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
    
print(mayor_edad(int(input("Cual es tu edad?: "))))


#La serie de fibonacci