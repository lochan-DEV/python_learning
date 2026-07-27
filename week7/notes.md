Function	|Purpose
re.match()	- Checks for a match only at the start of the string
re.search()	- Scans the whole string, returns first match
re.findall() - Returns all matches as a list of strings
re.finditer() - Returns an iterator of match objects (all matches)
re.sub() - Replaces matches with a string
re.split() - Splits string by the pattern
re.fullmatch() - Entire string must match the pattern




| Symbol           | Meaning                      
| ---------------- | ---------------------------- 
| `r""`            | Raw string                   
| `^`              | Start of string              
| `$`              | End of string                
| `.`              | Any character except newline 
| `\.`             | Literal dot                  
| `()`             | Group                                                 
| `*`              | 0 or more                    
| `+`              | 1 or more                    
| `?`              | Optional (0 or 1)            
| `{n}`            | Exactly n                    
| `{n,}`           | At least n                   
| `{n,m}`          | Between n and m              
| `\d`             | Digit                        
| `\D`             | Not a digit                  
| `\w`             | Word character               
| `\W`             | Not a word character         
| `\s`             | Whitespace                   
| `\S`             | Not whitespace               
| `re.search()`    | Search anywhere              
| `[]`             | character class
| `[^]`            | negelated character class
| `()`	           |Grouping
| `\d`	           |Digit [0-9]
| `\D`             |Non-digit