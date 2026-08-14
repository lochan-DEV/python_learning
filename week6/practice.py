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