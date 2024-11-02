import pytest
from numb3rs import validate


def test_validate():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"254.20.45.3") == True
    assert validate(r"256.256.256.256") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"True") == False
    assert validate(r"254.2000.45.3") == False
    assert validate(r"256.0.0.0") == False
    assert validate(r"2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate(r"255.0.0.0.0") == False
    assert validate(r"255.0..0") == False
    assert validate(r"255.256.0.0") == False
    assert validate(r"255.255.256.0") == False
    assert validate(r"255.255.255.256") == False
