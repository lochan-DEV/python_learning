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
