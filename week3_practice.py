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