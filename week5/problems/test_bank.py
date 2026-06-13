from bank import value          

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