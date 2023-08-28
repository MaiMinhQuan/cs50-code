from numb3rs import  validate

def main():
    test_hl()
    test_khls()
    test_khlc()

def test_hl():
    assert validate("1.2.3.4") == True
    assert validate("50.26.255.100") == True

def test_khls():
    assert validate("256.1.5.59") == False
    assert validate("-1.6.9.213") == False

def test_khlc():
    assert validate("cat") == False
    assert validate("1.2.3.5.6") == False

if __name__ == "__main__":
    main()