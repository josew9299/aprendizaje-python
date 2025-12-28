#El juego genera un número entre 1 y 100
#El usuario ingresa un númeor mediante un mensaje en la consola
#El programa responde con pistas: "Demasiado alto", "Demasiado bajo", o "¡Correcto!".
#Lleva un conteo de intentos hasta que el usuario adivine.
#Pregunta si el usuario quiere jugar otra vez.
import random

def jugar_adivinanza():
    # Generar número secreto entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0  # Contador de intentos
    
    print("¡He pensado en un número entre 1 y 100! ¡Adivina cuál es!")
    
    # Bucle para los intentos
    while True:
        try:
            # Pedir entrada al usuario
            adivinanza = int(input("Adivina el número (1-100): "))
            intentos += 1  # Incrementar intentos
            
            # Validar rango
            if adivinanza < 1 or adivinanza > 100:
                print("Número no válido, debe estar entre 1 y 100.")
                intentos -= 1  # No contar intentos inválidos
                continue
            
            # Comparar con el número secreto
            if adivinanza == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                print("Demasiado bajo.")
                
        except ValueError:
            print("Por favor, ingresa un número válido.")
            intentos -= 1  # No contar intentos inválidos

# Bucle principal para jugar de nuevo
while True:
    jugar_adivinanza()  # Iniciar una partida
    # Preguntar si quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar otra vez? (sí/no): ").lower()
    if jugar_de_nuevo not in ["sí", "si", "s"]:
        print("¡Gracias por jugar!")
        break