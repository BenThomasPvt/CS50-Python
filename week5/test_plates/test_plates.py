from plates import is_valid


def test_1():
    assert is_valid("CS50") == True


def test_2():
    assert is_valid("5S50") == False  # Starts with a number


def test_21():
    assert is_valid("5550") == False  # Starts with a number


def test_3():
    assert is_valid("CS05") == False  # Number starts with '0'


def test_4():
    assert is_valid("CS50P") == False  # Too long


def test_5():
    assert is_valid("PI3.14") == False  # Invalid character '.'


def test_6():
    assert is_valid("H") == False  # Too short


def test_7():
    assert is_valid("OUTATIME") == False  # Too long
