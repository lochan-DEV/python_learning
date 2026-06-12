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

if __name__ == "__main__":
    main()

# to test the above function

from twttr import shorten        # this code is used to test the above function

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("123456") == "123456"

def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"

def test_empty():
    assert shorten("") == ""


#########################################################################################



