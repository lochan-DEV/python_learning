def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(x):
    if len(x)<2 or len(x)>6:
        return False
    if not x[0:2].isalpha():
        return False
    if not x.isalnum():
        return False
    for i in range(len(x)):
        if x[i].isdigit():
            if x[i]=="0":
                 return False
            if not x[i:].isdigit():
                return False
            break
    return True


if __name__=="__main__":
    main()
