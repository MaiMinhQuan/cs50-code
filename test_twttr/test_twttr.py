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

if __name__ == "__main__":
    main()