import pytest
from fuel import convert,gauge

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4 / 0")


def test_ValueError():
    with pytest.raises(ValueError):
        convert("Cat/Cat")

def test_input():

    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/3") == 33 and gauge(33) == "33%"
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("4/4") == 100 and gauge(100) == "F"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("0/4") == 0 and gauge(0) == "E"
    assert convert("1/100") == 1 and gauge(1) == "E"
