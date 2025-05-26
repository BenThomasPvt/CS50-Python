from twttr import shorten


def test_shorten():
    assert shorten("Hello there") == "Hll thr"


def test_capital():
    assert shorten("Oi HOMELANDER") == " HMLNDR"


def test_numbers():
    assert shorten("L1fe i5 5h0rt") == "L1f 5 5h0rt"


def test_pun():
    assert shorten("Hello, There!") == "Hll, Thr!"
