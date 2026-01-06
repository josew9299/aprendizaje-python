# ¡Prueba Git con este código! Guárdalo como hola.py
# ¡Prueba Git con este código! Guárdalo como hola.py
# hola.py
from datetime import datetime
import random
print("Git está funcionando correctamente :)")
print("Este archivo está en la carpeta 00_FUNDAMENTOS")

# Bonus: Prueba este código en otro archivo (ej: 00_FUNDAMENTOS/fecha.py)

print(f"¡Hoy es {datetime.now().strftime('%d/%m/%Y')} y Git funciona!")
""""""
x = 0
while x <= 200:
    if x == 150:
        print(x,"Excellent")
    else:
        print(x)
    x +=1


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