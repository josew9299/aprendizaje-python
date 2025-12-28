# Juego de Piedra, Papel o Tijera en Python, implementado con validación robusta, puntajes modulares y mensajes claros.
import json
import random
p_p_t = ["Piedra", "Papel", "Tijera"]
puntaje_user = 0
puntaje_compu = 0

def guardar_puntajes():
    """Guarda los puntajes en un archivo Json."""
    puntajes = {"usuario": puntaje_user, "Computadora": puntaje_compu}
    with open("puntajes.json", "w") as file:
        json.dump(puntajes, file)


def compu_w():
    print("La computadora gana!")
def user_w():
    print("Tú ganas!")
def tie():
    print("Ha habido un empate parcial")

def puntaje():
    global puntaje_user, puntaje_compu
    print(f"Puntaje: Tú - {puntaje_user}, Computadora - {puntaje_compu}")

def jugar():
    # Entrada del usuario y elección de la computadora
    elec_usuario = input("Ingresa \"Piedra\", \"Papel\" o \"Tijera\": ")
    elec_usuario = elec_usuario.title()
    compu = random.choice(p_p_t)
    # Usar puntajes globales
    global puntaje_user, puntaje_compu
    try:
        # Validar entrada del usuario
        while elec_usuario not in p_p_t:
            elec_usuario = input("Ingresa \"Piedra\", \"Papel\" o \"Tijera\": ")
            elec_usuario = elec_usuario.title()
            print("Entrada no válida, ingresa 'Piedra', 'Papel' o 'Tijera'")
        # Imprimir elección de usuario y computadora
        print(f"La computadora eligió: {compu}")
        print(f"Tú elegiste: {elec_usuario}")
        # Compara las elecciones y da el veredicto
        if compu == "Tijera" and elec_usuario == "Piedra" or compu == "Piedra" and elec_usuario == "Papel" or compu == "Papel" and elec_usuario == "Tijera":
            user_w()
            puntaje_user += 1
        if compu == "Tijera" and elec_usuario == "Papel" or compu == "Piedra" and elec_usuario == "Tijera" or compu == "Papel" and elec_usuario == "Piedra":
            compu_w()
            puntaje_compu += 1
        if compu == elec_usuario:
            tie()
        puntaje()
    except ValueError as e:
        print(f"Error{e}, ingresa 'Piedra', 'Papel' o 'Tijera'")

print("¡Bienvenido a Piedra, Papel o Tijera!")

# Resto del código igual, pero añade la llamada a guardar_puntajes() al final del bucle principal
while True:
    jugar()
    jugar_de_nuevo = input("¿Jugar otra ronda? (sí/s/no/n): ")   
    jugar_de_nuevo = jugar_de_nuevo.lower()
    while jugar_de_nuevo not in ["sí", "s", "no", "n"]:
        print("Entrada no válida, ingresa 'sí', 's', 'no', o 'n'")
        jugar_de_nuevo = input("¿Jugar otra ronda? (sí/s/no/n): ")
        jugar_de_nuevo = jugar_de_nuevo.lower()
    if jugar_de_nuevo in ["no", "n"]:
        guardar_puntajes() #Guardar al salir
        break

puntaje()
print("¡Hasta luego!")
input("")

# Completado: Validación de entrada, elección de computadora, comparaciones simplificadas, puntajes actualizados (Partes 1-4).
# Completado: Bucle principal para múltiples rondas con validación robusta de 'jugar_de_nuevo' y mensajes claros con formato estandarizado (Parte 5).
# Completado: Añadida función puntaje para mostrar puntajes de forma consistente y modular.
# Finalizado: Juego completamente funcional con mensajes consistentes, validación optimizada y correcciones estilísticas.