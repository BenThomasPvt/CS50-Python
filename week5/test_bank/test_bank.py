from bank import value

def test_zero():
    assert value("hello there") == 0

def test_20():
    assert value("hey there") == 20

def test_hun():
    assert value("what up") == 100

def test_case():
    assert value("Hello There") == 0
