from ejercicios_basicos import mayor_edad
ver = int(input("Cuantos años tienes?: "))

mayor_edad(ver)

if mayor_edad(ver) is True:
    print("Excelente, la función está funcionando correctamente!✅")
else:
    print("Error")