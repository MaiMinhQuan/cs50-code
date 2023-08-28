from numb3rs import  validate

def main():
    test_hl()
    test_khl()

def test_hl():
    assert validate(r"1.2.3.4") == True
    assert validate(r"50.26.255.100") == True
    assert validate(r"15.56.89.13") == True

def test_khl():
    assert validate(r"256.1.5.59") == False
    assert validate(r"1000.6.9.213") == False
    assert validate(r"cat") == False
    assert validate(r"1") == False
    assert validate(r"2.3.4") == False
    assert validate(r"1.2") == False
    assert validate(r"45.56") == False


if __name__ == "__main__":
    main()