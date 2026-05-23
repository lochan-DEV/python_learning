# practice code for week 3 - exceptions

# calculator program with exception handling
def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")

            result = num1 / num2
            print(f"The result is: {result}")
            break

        except ZeroDivisionError as e:
            print(f"Math error: {e}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()



#asking user for age with exception handling
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")

except ValueError:
    print("That's not a valid age!")



#square and cube calculator with exception handling
try:
    num = int(input("Enter a number: "))
    print(f"The square of {num} is {num ** 2} and the cube of {num} is {num ** 3} ")
except ValueError:
    print("That's not a valid number!")
    
