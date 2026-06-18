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