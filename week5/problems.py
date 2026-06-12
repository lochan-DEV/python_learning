# problem 1 - testing the shorten function
    
def main():                              
    x = input("Input: ")                 
    print("Output:", shorten(x))



def shorten(text):
    vowels = "aeiouAEIOU"
    result = ""

    for c in text:
        if c not in vowels:
            result += c

    return result


# to test the above function

