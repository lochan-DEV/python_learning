#problem 1 of week 2
x=input("camelCase :")
result=""
for c in x:
    if c.isupper():
        result=result+"_"+c.lower()

    else:
        result=result+c
print("snake_case :", result)