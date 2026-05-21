#problem 1 of week 2
x=input("camelCase :")
result=""
for c in x:
    if c.isupper():
        result=result+"_"+c.lower()

    else:
        result=result+c
print("snake_case :", result)



#problem 2
amount_due=50
while amount_due>0:
    print("amount_due :", amount_due)
    x=int(input("Insert Coin: "))
    if x in [25,10,5]:
        amount_due=amount_due-x
    else:
        print("hey fool wrong coin")

print("change_owed :", abs(amount_due))



#problem 3
vowels=["a","e","i","o","u","A","E","I","O","U"]
x=input("enter a sentence :")
result=""
for c in x:
    if c not in vowels:
        result=result+c
print("output :", result)



#problem 4
def main():
    plates=input("enter the plate number :")
    if is_valid(plates):
        print("valid")
    else:
        print("invalid")
def is_valid(x):
    if len(x)<2 or len(x)>6 :
        return False
    if not x.isalnum():
        return False
    if not x[0:2].isalpha():
        return False
    for i in range(len(x)):
        if x[i].isdigit():
            if x[i]=="0":
                return False
            if not x[i:].isdigit():
                return False
            break
    return True
main()



#problem 5
nutri={"apple":"130","banana":"110","chocolate":"","avocado":"50","kiwifruit":"90",
       "pear":"100","sweet cherries":"100"}
x=input("item :").strip().lower()
if x in nutri:
    print("calories :", nutri[x])
else:
    print("check youerself idiot ")
   