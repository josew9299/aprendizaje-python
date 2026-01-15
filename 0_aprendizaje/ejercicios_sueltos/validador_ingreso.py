"""
🧩 Enunciado

Vas a crear un programa que:

Pida al usuario:

su nombre

su edad

si tiene permiso (sí / no)

El programa debe decidir si la persona:

✅ puede ingresar

❌ no puede ingresar

🧠 Reglas de decisión

La persona puede ingresar solo si:

tiene 18 años o más

Y su permiso es "sí"

En cualquier otro caso:

no puede ingresar

📌 Reglas del reto

❌ No uses funciones

❌ No uses listas

❌ No uses bucles

❌ No copies código de internet

✅ Usa solo input, print, if, elif, else

🎯 Salida esperada (ejemplo)

Si el usuario escribe:

Nombre: Ana
Edad: 20
Permiso: sí


El programa muestra:

Ana puede ingresar.


Si no cumple:

Ana no puede ingresar.
"""

nombre = input("Cual es tu nombre?: ").title()
edad = int(input("Cual es tu edad?: "))
permiso = input("Tienes permiso? (Si/No): ").strip().lower()

def validar_ingreso(nombre,edad,permiso):
    permiso = permiso.strip().lower()
    if edad < 0:
        return "Edad inválida"
    if permiso not in ("si","sí"):
        return f"❌ {nombre} no puede ingresar"
    if edad >=18:
        return f"✅ {nombre} puede ingresar"

    else:
        return f" ❌ {nombre} no puede ingresar"
    
print(validar_ingreso(nombre,edad,permiso))