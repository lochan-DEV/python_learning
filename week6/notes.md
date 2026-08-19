# File :
A file is a storage unit used to save data permanently.
Data in variables is temporary → lost after program ends
Data in files → remains saved

# to open files and to access it :
 using ("with") function you can open files and it auomaticalliy closes itself 
   eg; with open(file_name,"access_mode") as file:

# access modes:     Mode	   Meaning
                    "r"  	   Read
                    "w" 	   Write (overwrites)
                    "a"	       Append (adds data at last or at the end of the file)


# What is CSV?

 CSV = Comma-Separated Values
       It is a simple format used to store tabular data.


# What is CSV?

 CSV = Comma-Separated Values

 It is a simple format used to store tabular data.

Example books.csv:

title,year
1984,1949
Atomic Habits,2018
Deep Work,2016

 Think of it like an Excel table:

title	year
1984	1949
Atomic Habits	2018
Deep Work	2016

CSV is mainly useful when your data looks like rows and columns.

