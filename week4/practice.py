# practicing using libraries 

# to give random numbers as output --

import random


num = random.randint(1, 50)
print(f"Random number: {num}")
print("Even" if num % 2 == 0 else "Odd")


# hello message with animals --
import cowsay     # cowsay module need to be installed first [pip install cowsay]

animals = {
    "cow": cowsay.cow,
    "tux": cowsay.tux,
    "dragon": cowsay.dragon,
    "ghostbusters": cowsay.ghostbusters,
    "kitty": cowsay.kitty,
    "meow": cowsay.meow,
    "stegosaurus": cowsay.stegosaurus}

x = input("enter animal name: ").lower()

if x in animals:
    animals[x]("hello")
else:
    print("animal not found")




# Shuffle a deck (simplified) ----
import random
cards = ["Ace", "King", "Queen", "Jack", "10"]
print("Before shuffle:", cards)
random.shuffle(cards)
print("After shuffle :", cards)


# rock, paper, scissors game --

import random
import sys

choices = ["rock", "paper", "scissors"]
if len(sys.argv) < 2:
    sys.exit("Error: Please provide your choice. Example: python game.py rock")
x= sys.argv[1].lower().strip()
if x not in choices:
    sys.exit("Error: Invalid choice. Choose rock, paper, or scissors.")
y = random.choice(choices)
print(f"Your choice:     {x}")
print(f"Computer choice: {y}")
if x == y:
    print("It's a tie!")
elif (x == "rock" and y == "scissors") or \
     (x == "paper" and y == "rock") or \
     (x == "scissors" and y == "paper"):
    print("You win!")
else:
    print("Computer wins!")



# coin flip --

import random
list = ["heads", "tails"]

while True:
    x= input("Bet heads or tails (or type 'quit' to stop): ").lower().strip()
    if x=="quit":
        print("Thanks for playing!")
        break
    if x not in list:
        print("Invalid choice. Please type 'heads' or 'tails'.\n")
        continue
    coin_result = random.choice(list)
    print("  Coin flip results")
    print(f"Your Bet:    {x.capitalize()}")
    print(f"Flip Result: {coin_result.capitalize()}")
   
    if x == coin_result:
        print("You won the bet!")
    else:
        print(" You lost. Better luck next time!")


# accepts user name in command line argument
import sys

if len(sys.argv)<2:
    print("Too few arguments")
    sys.exit(1)
elif len(sys.argv)>2:
    print("Too many arguments")
    sys.exit(1)
else:
    print("hello", sys.argv[1])  
    