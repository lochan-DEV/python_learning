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



# problem 3-file extension
x=input("enter the file name:").lower().strip()
if x.endswith(".gif"):
    print("image/gif")
elif x.endswith(".jpg"):
    print("image/jpeg")
elif x.endswith(".jpeg"):
    print("image/jpeg")
elif x.endswith(".png"):
    print("image/png")
elif x.endswith(".pdf"):
    print("application/pdf")
elif x.endswith(".txt"):
    print("text/plain")
elif x.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")




#problem 4-math interpreter
user=input("enter the expression:")
x,y,z=user.split(" ")
x=float(x)
z=float(z)
if y=="+":
    s=x+z
    print("sum", s)
elif y=="-":
    d=x-z
    print("difference", d)
elif y=="*":
    p=x*z
    print("product", p)
elif y=="/":
    q=x/z
    print("quotient", q)
else:
    print("ha ha ha")




# problem 5- meal time
def main():
    x=input("enter the time:")
    time=convert(x)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        print("snack time")

def convert(time):
    hours,minutes=time.split(":")
    hours=float(hours)
    minutes=float(minutes)
    return hours + (minutes/60.0)

if __name__ == "__main__":
    main()