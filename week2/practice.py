# multiplication table using for loop
n=int(input("enter a number: "))
for i in range(11):
    print(n ,"*", i ,"=", n*i)



# password access using while loop
x=input("enter the password: ")
while True:
    if x=="coder":
        print("access granted")
        break
    else: 
        print("wrong password stranger")
        x=input("enter the password: ")




#coding using the list data structure
names=["lochan", "sathya", "kishore"]
for name in names:
    print(name , sep="\n")


# password creation 
def main():
    x=password()
    print("your password is: ", x)

def password():
   
    while True:
         x=input("enter password: ")
         if len(x)!=6 or len(x)>6:
             print("password must be 6 characters long")
         elif x[0].islower():
             print("password must start with a capital letter")
         elif x[5].isalpha():
             print("password must end with a number")
         elif len(x)==4 or len(x)<4:
                print("password must be 6 characters long")
                continue
         else:
             break
    return x
if __name__ == "__main__":
    main()



# guessing game
secret = 7
while True:
    guess = int(input("Guess a number 1-10: "))
    if guess == secret:
        print("You got it!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

