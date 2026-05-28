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