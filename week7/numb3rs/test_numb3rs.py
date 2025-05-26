from numb3rs import validate
import sys


def test_valid_ip_0():
    assert validate(r"127") == False


def test_valid_ip():
    assert validate(r"255.255.255.255") == True


def test_invalid_ip_1():
    assert validate(r"512.512.512.512") == False


def test_invalid_ip_2():
    assert validate(r"1.2.3.512") == False


def test_invalid_input():
    assert validate(r"cat") == False


if __name__ == "__main__":
    test_valid_ip_0()
    test_valid_ip()
    test_invalid_ip_1()
    test_invalid_ip_2()
    test_invalid_input()
