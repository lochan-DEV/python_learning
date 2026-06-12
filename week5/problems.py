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


# problem 2 - testing the value function 

def main():
    x = input("Enter the sentence: ").strip()
    result = value(x)
    print("Output:", result)


def value(x):
    x = x.lower().strip()  

    if x.startswith("hello"):
        return "$0"
    elif x.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()


# to test the above function 

from bank import value           # this code is used to test the above function

def test_hello():
    assert value("hello") == "$0"

def test_hello_phrase():
    assert value("hello there") == "$0"

def test_case_insensitive():
    assert value("HELLO") == "$0"

def test_h_greeting():
    assert value("hey") == "$20"

def test_h_uppercase():
    assert value("Hey!") == "$20"

def test_other():
    assert value("what's up") == "$100"

def test_empty():
    assert value("") == "$100"




