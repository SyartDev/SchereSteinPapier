import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

fotos = [rock, paper, scissors]
spieler_wahl  = int(input("Was wählst du?: (help, 0, 1, 2)\n").lower())
print(fotos[spieler_wahl])

computer_wahl = random.randint(0,2)
print("Computer wählt: ")
print(fotos[computer_wahl])



if spieler_wahl == "help":
    print("0 = Rock, 1 = Paper, 2 = Scissors")
    exit()
if int(spieler_wahl) >= 3 or int(spieler_wahl) < 0 :
    print("Ungültige Eingabe")
    exit()

spieler_wahl = int(spieler_wahl)

if spieler_wahl == 0 and computer_wahl == 2:
    print("Du gewinnst!")
elif computer_wahl == 0 and spieler_wahl == 2:
    print("Computer gewinnt!")
elif computer_wahl > spieler_wahl:
    print("Computer gewinnt!")
elif spieler_wahl > computer_wahl:
    print("Du gewinnst!")
else:
    print("Unentschieden!")    
