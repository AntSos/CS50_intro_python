from bank import value

def test_0_return():

    assert value("Hello there") == 0
    assert value ("hello sir") == 0
    assert value ("HelLo sIr") == 0

def test_20_return():

    assert value("Hi there") == 20
    assert value("Haloja") == 20
    assert value("Hola") == 20


def test_100_return():

    assert value("Whats up") == 100
    assert value("Whats the matter pumpking") == 100
    assert value("Aloja") == 100
