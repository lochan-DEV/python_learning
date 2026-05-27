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
