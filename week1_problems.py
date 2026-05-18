#problem 1 deep thought
x=input("what is the answer? ").lower().strip()
if x=="42":
    print("yes")
elif x=="forty two":
    print("yes")
elif x=="forty-two":
    print("yes")
else:
    print("no")
