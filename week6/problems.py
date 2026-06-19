# problem - 1

import sys

def main():
    is_valid()
    count=check_len()
    print(count)

def is_valid():
        if len(sys.argv)<2:
            sys.exit("too few command line arguments")
        elif len(sys.argv)>2:
            sys.exit("too many command line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a python file")
        else:
            try:
                with open(sys.argv[1]) as f:
                    pass
            except FileNotFoundError:
                sys.exit("File does not exist")

def check_len():
    count = 0
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue
            elif line.startswith("#"):
                continue
            else:
                count =count+1

    return count


if __name__=="__main__":
    main()

##################################################################

# problem - 2 

import sys
import csv
from tabulate import tabulate


def main():
     is_valid()
     content=read_file()
     print(content)



def is_valid():
        if len(sys.argv)<2:
            sys.exit("too few command line arguments")
        elif len(sys.argv)>2:
            sys.exit("too many command line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            try:
                with open(sys.argv[1]) as f:
                    pass
            except FileNotFoundError:
                sys.exit("File does not exist")

def read_file():
     table=[]
     with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        return tabulate(table, headers="firstrow", tablefmt="grid")

if __name__=="__main__":
     main()

