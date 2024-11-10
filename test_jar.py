from jar import Jar


def test_init():
    jar_01 = Jar(3)
    assert jar_01.capacity == 3
    jar_02 = Jar(6)
    assert jar_02.capacity == 6
    jar_03 = Jar(9)
    assert jar_03.capacity == 9
    jar_04 = Jar()
    assert jar_04.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar_01 = Jar()
    jar_01.deposit(12)
    assert jar_01.size == 12
    jar_02 = Jar()
    jar_02.deposit(6)
    assert jar_02.size == 6
    jar_03 = Jar()
    jar_03.deposit(3)
    assert jar_03.size == 3


def test_withdraw():
    jar_01 = Jar()
    jar_01.deposit(12)
    jar_01.withdraw(6)
    assert jar_01.size == 6
    jar_02 = Jar()
    jar_02.deposit(12)
    jar_02.withdraw(3)
    assert jar_02.size == 9
    jar_03 = Jar()
    jar_03.deposit(12)
    jar_03.withdraw(9)
    assert jar_03.size == 3
