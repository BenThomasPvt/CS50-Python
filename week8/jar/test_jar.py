from jar import Jar

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    try:
        Jar(-1)  # This should raise a ValueError
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    try:
        jar.deposit(6)  # Exceeds capacity, should raise ValueError
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"
    jar.deposit(4)
    assert jar.size == 9  # Total cookies: 9

def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    try:
        jar.withdraw(8)  # Not enough cookies, should raise ValueError
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"
    jar.withdraw(5)
    assert jar.size == 2  # Total cookies after withdrawal: 2

def test_capacity():
    jar = Jar(5)
    assert jar.capacity == 5
    try:
        jar.capacity = -3  # Invalid capacity, should raise ValueError
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised"
    jar.capacity = 8
    assert jar.capacity == 8

