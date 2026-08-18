# practicing csv
import csv
books = [
    {"title": "1984", "author": "Orwell", "year": 1949},
    {"title": "Sapiens", "author": "Harari", "year": 2011},
    {"title": "Dune", "author": "Herbert", "year": 1965},
]


with open("books.csv","w") as f:
    fieldnames=["title","author","year"]
    writer=csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(books)


with open("books.csv","r") as f:
    read=csv.DictReader(f)
    for row in read:
        print(row)


# storing a students record and accessing it for particular operations
students = [
    {"name": "Ravi", "marks": 88, "grade": "A"},
    {"name": "Meena", "marks": 45, "grade": "F"},
    {"name": "Kiran", "marks": 76, "grade": "B"},
]

with open("stu.csv","w",newline="") as f:
    x=["name","marks","grade"]
    writer=csv.DictWriter(f, fieldnames=x)
    writer.writeheader()
    writer.writerows(students)

with open("stu.csv","r") as f:
    reader=csv.DictReader(f)
    data=list(reader)
    print(data)

for row in data:
    row["marks"]=int(row["marks"])

top=max(data, key=lambda d: d["marks"])
print(f"Topper name is  {top["name"]} scored {top["marks"]} marks ")

for row in data:
    if row["name"]=="Meena":
        row["grade"]="repeat"


with open("stu.csv","w",newline="") as f:
    x=["name","marks","grade"]
    writer=csv.DictWriter(f , fieldnames=x)
    writer.writeheader()
    writer.writerows(data)

with open("stu.csv","r") as f:
    reader=csv.DictReader(f)
    data=list(reader)
print(data)


# practicing json
import json

books = [
    {"title": "1984", "author": "Orwell", "year": 1949, "issued": False},
    {"title": "Sapiens", "author": "Harari", "year": 2011, "issued": True},
    {"title": "Dune", "author": "Herbert", "year": 1965, "issued": False},
]


with open("book.json","w") as f:
    json.dump(books,f,indent=4)

with open("book.json","r") as f:
    data=json.load(f)
    print(data)

