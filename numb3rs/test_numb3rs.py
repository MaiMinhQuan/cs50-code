from numb3rs import  validate

def main():
    test_hl()
    test_khl()

def test_hl():
    assert validate("1.2.3.4") == True
    assert validate("50.26.255.100") == True
    assert validate("15.56.89.13") == True

def test_khl():
    assert validate("256.1.5.59") == False
    assert validate("1000.6.9.213") == False
    assert validate("cat") == False
    assert validate("1") == False
    assert validate("9.8.56") == False
    assert validate("5.6") == False
    assert validate("45.1568") == False


if __name__ == "__main__":
    main()