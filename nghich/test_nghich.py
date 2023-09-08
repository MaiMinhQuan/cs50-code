from nghich import check_name, day_convert, time_convert

def test_check_name():
    assert check_name("Quan") == True
    assert check_name(" vu trong  phung") == True
    assert check_name("Mai2004") == False
    assert check_name("vu-1945") == False
    assert check_name("2john?") == False
    assert check_name("*josh") == False

def test_day_convert():
    assert day_convert("Monday") == 1
    assert day_convert("Tuesday") == 2
    assert day_convert("Wednesday") == 3
    assert day_convert("Thursday") == 4
    assert day_convert("Friday") == 5
    assert day_convert("Saturday") == 6
    assert day_convert("Sunday") == 7
    assert day_convert("Momday") == "Day is invalid"

def test_time_convert():
    assert time_convert("Morning") == 1
    assert time_convert("Afternoon") == 2
    assert time_convert("Evening") == 3
    assert time_convert("Noon") == "Time is invalid"