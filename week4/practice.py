# practicing using libraries 

# to give random numbers as output

import random

import pip
num = random.randint(1, 50)
print(f"Random number: {num}")
print("Even" if num % 2 == 0 else "Odd")

#

import cowsay

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
