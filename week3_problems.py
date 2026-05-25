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



#problem 3
dict={}
while True:
    try:
        x=input()
        if x in dict:
            dict[x]=dict[x]+1
        else:
            dict[x]=1

    except EOFError:
        break

for y in sorted(dict):
    print(f"{dict[y]} {y.upper()}")




# problem 4
dict={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12}
while True:
    x=input("date :").strip()

    try:
        if x[0].isdigit():
            a,b,c=x.split("/")
            if int(a)>12 or int(b)>31:
                raise ValueError
            print(f"{c}-{int(a):02}-{int(b):02}")
            break
        elif x[0].isalpha():
            a,b,c=x.split(" ")
            b=b.strip(",")
            if a  not in dict or int(b)>31:
                raise ValueError
            elif "," not in x:
                raise ValueError
            print(f"{c}-{dict[a]:02}-{int(b):02}")
            break
    except (ValueError,KeyError):
        pass
