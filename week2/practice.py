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
