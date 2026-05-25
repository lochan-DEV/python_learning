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
