from numb3rs import  validate

def main():
    test_hl()
    test_khl()

def test_hl():
    assert validate(r"12.26.35.84") == True
    assert validate(r"48.62.49") == False
    assert validate(r"99.66") == False
    assert validate(r"8") ==False

def test_khl():
    assert validate(r"100.100.100.100") == True
    assert validate(r"1000.6.9.213") == False
    assert validate(r"100.5641.26.59") == False
    assert validate(r"1.666.666.777") == False
    assert validate(r"45.16.7895.23") == False


if __name__ == "__main__":
    main()