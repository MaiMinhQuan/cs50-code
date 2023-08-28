from working import convert
import pytest

def main():
    test_hl()
    test_saiform()
    test_saigio()
    test_saiphut()

def test_hl():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("7:19 AM to 1:27 PM") == "07:19 to 13:27"

def test_saiform():
    with pytest.raises(ValueError):
        convert("7 AM - 6PM")
        convert("9:30 AM : 5:19 PM")

def test_saigio():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
        convert("9: 45 AM to 13 PM")

def test_saiphut():
    with pytest.raises(ValueError):
        convert("9:61 AM to 5 PM")
        convert("8 AM to 6:90 PM")

if __name__ == "__main__":
    main()