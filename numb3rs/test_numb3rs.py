from numb3rs import  validate

def main():
    test_hl()
    test_khl()

def test_hl():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"cat") ==False

def test_khl():
    assert validate(r"256.1.5.59") == False
    assert validate(r"1000.6.9.213") == False
    assert validate(r"100.5641.26.59") == False
    assert validate(r"1.2.3.1597") == False
    assert validate(r"45.16.7895.23") == False
    assert validate(r"45.56") == False


if __name__ == "__main__":
    main()