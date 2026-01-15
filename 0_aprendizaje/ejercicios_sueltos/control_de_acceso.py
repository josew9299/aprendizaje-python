

nombre = input("Cual es tu nombre?: ")
edad = int(input("Cual es tu edad?: "))
permiso = str(input("Tienes permiso?: "))
continuar = True

def control_ingreso(nombre,edad,permiso):
    permiso = permiso.strip().lower()
    nombre = nombre.title()
    
    if edad <= 0 or edad >120:
        return "Edad inválida"
    
    if permiso not in ("si","sí","no"):
        return "Permiso no válido"
    
    if edad >= 18 and permiso in ("si","sí"):
        return f" ✅ {nombre} puede ingresar"
    
    else:
        return f"❌ {nombre} no puede ingresar"

continuar = True


while continuar:
    
    respuesta = input("Desea verificar otra persona? (s/n): ").strip().lower()
    
    if respuesta == "n":
        print("Muchas gracias, hasta luego!")
        continuar = False
    
    elif respuesta == "s":
        nombre = input("Cual es tu nombre?: ")
        edad = int(input("Cual es tu edad?: "))
        permiso = str(input("Tienes permiso?: "))
        
        resultado = control_ingreso(nombre,edad,permiso)
        print(resultado)
        
    else:
        print("Opción no válida. Use `s` o `n`")