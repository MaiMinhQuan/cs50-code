from plates import is_valid

def main():

def test_2start():
    assert is_valid("AA563") == True
    assert is_valid("A563") == False

def test_len():
    assert is_valid("M") == False
    assert is_valid("A498662") == False

def test_numal():
    assert is_valid("AA5O") == False

def test_al0():
    assert is_valid("VD0") == False

def test_dau():
    assert is_valid("AS<>") == False

if __name__ == "__main__":
    main()