from plates import is_valid

def test_is_valid():

    assert is_valid("HELLO")==True
    assert is_valid("HELLO, WORLD")==False
    assert is_valid("CS50")==True
    assert is_valid("GOODBYE")==False
    assert is_valid("CS05")==False
    assert is_valid("50")==False
    assert is_valid("CS,.0")==False
    assert is_valid("CS50P")==False
    assert is_valid("AS ASD")==False
    assert is_valid("CS#$SD0")==False
    