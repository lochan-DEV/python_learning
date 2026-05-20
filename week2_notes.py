# Week 2 - Loops and Data Structures

#day 1 of learning loops in python

# FOR LOOP - [used when you know how many times to repeat]
for i in range(5):
    print(i)  # prints 0,1,2,3,4

# WHILE LOOP - [used when you don't know how many times]
while True:
    name = input("Enter name: ")
    if name != "":
        break

# RANGE - generates numbers
range(5)      # 0,1,2,3,4
range(1,6)    # 1,2,3,4,5
range(0,10,2) # 0,2,4,6,8

# LIST - stores multiple values
names = ["lochan", "david", "john"]

# DICT - stores key:value pairs
student = {"name": "lochan", "age": 18}

# LEN - counts length
len(names)  # 3