import random
import math
#Rock, paper, scissors  My version

player_1 = ("rock", "paper", "scissors")
player_2 = ("rock", "paper", "scissors")

p1 = random.choice(player_1)
p2 = random.choice(player_2)

print(p1,p2)
#Draw
if p1 == "scissors" and p2 == "scissors":
    print("Draw!")
    
elif p1 == "rock" and p2 == "rock":
    print("Draw!")
    
elif p1 == "paper" and p2 == "paper":
    print("Draw!")
#Player_1 wins!
elif p1=="scissors" and p2 == "paper":
    print("Player 1 wins!")
elif p1 == "paper" and p2 == "rock":
    print("Player 1 wins!")
    
elif p1 == "rock" and p2 == "scissors":
    print("Player 1 wins!")
else:
    print("Player 2 wins")

#Rock, paper, scissors  MDeepSeek version

player_choices = ("rock", "paper", "scissors")

p1 = random.choice(player_choices)
p2 = random.choice(player_choices)

print(f"Player 1: {p1}, Player 2: {p2}")

# Empate (simplificado)
if p1 == p2:
    print("Draw!")
# Player 1 gana (condiciones agrupadas)
elif (p1 == "rock" and p2 == "scissors") or \
    (p1 == "paper" and p2 == "rock") or \
    (p1 == "scissors" and p2 == "paper"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")

calif_1 = float(input("Por favor ingrese su calificación: "))
calif_2 = float(input("Por favor ingrese su calificación: "))

def sum_calif(x, y):
    if isinstance(x,float):
        x = math.floor(x)
    if isinstance(y, float):
        y = math.floor(y)
    return x + y

resultado = sum_calif(calif_1,calif_2)
print("La suma redondeada es :",resultado)