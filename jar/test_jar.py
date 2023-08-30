from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity() == 12
    jar1 = Jar(5)
    assert jar.capacity() == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit()