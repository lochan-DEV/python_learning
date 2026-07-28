
def main():
    print("for example enter the list in this format = 3 4 5 6 34 456 12")
    x = input("enter list: ")
    x= x.split()
    x = [int(p) for p in x]
    print(find_max(x))


def find_max(x):
    
    max=x[0]
    for i in range(len(x)):
        if x[i]>max:
            max=x[i]
        else:
            pass
    return max

if __name__ == "__main__":
    main()
