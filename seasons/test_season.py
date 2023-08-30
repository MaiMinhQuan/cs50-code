from seasons import check_sn

def main():
    test_hl()
    test_khl()

def test_hl():
    assert check_sn("1945-09-02") == {"year":1945, "month":9, "day":2}

def test_khl():
    assert check_sn("August 22, 2004") == None
    assert check_sn("2000-1-1") == None
    assert check_sn("15 10 2010") == None

if __name__ == "__main__":
    main()
