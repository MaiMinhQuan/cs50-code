from um import count

def main():
    test_hl()
    test_dinh()
    test_hh()

def test_hl():
    assert count("um um um um") == 4
    assert count"..um..um....") == 2

def test_dinh():
    assert count("hum--hum++hum") == 0
    assert count("that dish is so yummy") == 0

def test_hh():
    assert count("um, i think that 's hard") == 1
    assert count("um..., um, inhale..") == 2

if __name__ == "__main__":
    main()