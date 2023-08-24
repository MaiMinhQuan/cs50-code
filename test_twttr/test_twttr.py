from twttr import shorten

def main():
    test_na()
    test_pa()
    test_dau()

def test_na():
    assert shorten("UUUUa") == ""
    assert shorten("ATCScsd") == "TCScsd"
    assert shorten("Twitter") == "Twttr"

def test_pa():
    assert shorten("klmnbg") == "klmnbg"
    assert shorten("qwrty") == "qwrty"

def test_dau():
    assert shorten(";.") == ";."
    assert shorten(",/") == ",/"

def test_so():
    assert shorten("1596") == "1596"
if __name__ == "__main__":
    main()