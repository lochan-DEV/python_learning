# problem 1 
def main():
    result = fuel()
    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{round(abs(result))}%")

def fuel():
    while True:
        try:
            a, b = input("fraction: ").split("/")
            a = int(a)
            b = int(b)
            if a < 0 or b <= 0:
                raise ValueError
            if a > b:
                raise ValueError
            result = (a / b) * 100
            return result
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()



# problem 2-
food={"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
total=0
while True:
    try:
        x=input("Item :")

        if x.title() in food:
            total=total+food[x.title()]
            print(f"Total: ${total:.2f}")
        else:
            print("Item: ")

    except ValueError:
        pass
    except EOFError:
        break
    except x not in food:
        pass
