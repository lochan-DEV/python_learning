#problem 1- deep thought
x=input("what is the answer? ").lower().strip()
if x=="42":
    print("yes")
elif x=="forty two":
    print("yes")
elif x=="forty-two":
    print("yes")
else:
    print("no")


#problem 2- bank 
x=input("enter the sentence:").lower().strip()
if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")