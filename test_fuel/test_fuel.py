from fuel import convert, gauge
import pytest

def main():
    test_ms()
    test_ve()
    test_ci()
def test_ms():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_ve():
    with pytest.raises(ValueError):
        convert("monkey/camel")

def test_ci():
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

if __name__ == "__main__":
    main()