# problem 1
import emoji

x=input("enter the name of an emoji: ")
result= emoji.emojize(x , language="alias")
print(result)


# problem 2 
import sys
import random
from pyfiglet import Figlet

if len(sys.argv)>3 or len(sys.argv)==2:
    sys.exit("invalid")
elif len(sys.argv)==1:
    figlet=Figlet()
    font=figlet.getFonts()
    f = random.choice(font)
    figlet.setFont(font=f)
    x= input("Input: ")
    print(figlet.renderText(x))


elif len(sys.argv)==3:
    figlet=Figlet()
    if sys.argv[1]!='-f' and sys.argv[1]!='--font':
        sys.exit("invalid")
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("invalid")
    else:

        figlet.setFont(font=sys.argv[2])
        x=input("input :")
        print(figlet.renderText(x))



# problem 3
import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

y = random.randint(1, n)

while True:
    try:
        x = int(input("Guess: "))
        if x < 1:
            continue
    except ValueError:
        continue

    if x == y:
        print("Just right!")
        break
    elif x > y:
        print("Too large!")
    else:
        print("Too small!")




# problem 4
import random

def main():
    n = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        correct = False
        for j in range(3):
            try:
                z = int(input(f"{x} + {y} = "))
                if z == x + y:
                    score += 1
                    correct = True
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        if not correct:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()