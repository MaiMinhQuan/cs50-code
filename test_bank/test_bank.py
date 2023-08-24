from bank import value
def main():
    test_hello()
    test_h()
    test_n()


def test_hello():
    assert value("hello, DAvid") == 0
    assert value("     hello") == 0

def test_h():
    assert value("how are you?") == 20
    assert value("how 's it going man?") == 20

def test_n():
    assert value("who are you?") == 100
    assert value("what 's up?") == 100
if __name__ == "__main__":
    main()