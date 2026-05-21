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