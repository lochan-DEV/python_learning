#week0   day 1  practice 

# asking user for name 
n=input("what is your name? ")
print("my name is", n) 
 

#greeting user
x=input("what is your name? ")
print("hello",  x)


#asking for age 
age=input("what is your age?")
print(f"you are {age}  years old")


# pracice using def function
def hello(x):
    print("hello", x)
name=input("enter your name:")
hello(name)

# using def function    
def sum(x,y):
    return x+y
b=int(input("enter first number:"))
a=int(input("enter the second number:"))
result=sum(b,a)
print("the sum is:", result)


# 
name = input("Enter your name: ")
print(f"Wow {name}, even my keyboard types better than you.")


# mars age calculator
# 2. Space Age Calculator
age = int(input("Your age on Earth: "))
mars_age = round(age / 1.88, 2)
print(f"On Mars you'd be {mars_age} years old!")