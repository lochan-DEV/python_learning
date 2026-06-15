import pytest
from fuel import convert,gauge


def test_convert_typical():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("2/3") == 67


def test_convert_zero_numerator():
    assert convert("0/100") == 0


def test_convert_equal_numerator_denominator():
    assert convert("4/4") == 100
    assert convert("1/1") == 100

def test_convert_raises_value_error_non_integer():
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("one/three")
    with pytest.raises(ValueError):
        convert("2/3.0")


def test_convert_raises_value_error_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("101/100")


def test_convert_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"

def test_convert_raises_value_error_negative():
    with pytest.raises(ValueError):
        convert("-1/4")