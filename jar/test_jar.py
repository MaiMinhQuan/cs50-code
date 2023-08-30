from jar import Jar

def test_init():
    jar1 = Jar(5)
    assert jar1.capacity() == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar.deposit(1)
    assert jar.size == 11

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2