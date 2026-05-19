#practice problem 1:
x=int(input("enter the marks:"))
if 90<= x <=100:
    print("A grade")
elif 80<= x <90:
    print("B grade")
elif 70<=x<80:
    print("C grade")
elif 60<=x<70:
    print("D grade")
else:
    print("fail")




#practice problem 2:
x=float(input("enter the number: "))
if x>0:
    print(f"the given number {x} is positive")
elif x<0:
    print(f"the given number {x} is negative")
else:
    print(f"the given number {x} is zero")


#practice problem 3:
x=float(input("enter the number: "))
y=float(input("enter the number: "))
if x>y:
    print(f"{x} is greater than {y}")
elif x<y:
    print(f"{y} is greater than {x}")
else:
    print(f"{x} and {y} are equal")


#practice problem 4: comparing three numbers
x=float(input("enter the number: "))
y=float(input("enter the number: "))
z=float(input("enter the number: "))
if x>y and X>z:
    print(f"{x} is the greatest number")
elif y>x and y>z:
    print(f"{y} is the greatest number")
elif z>x and z>y:
    print(f"{z} is the greatest number")
else:
    print("all numbers are equal")