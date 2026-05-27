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