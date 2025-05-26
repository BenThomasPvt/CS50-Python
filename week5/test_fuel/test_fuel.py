import sys
sys.path.append('.')
from fuel import convert, gauge
import pytest


def test_addition():
    assert 1 + 1 == 2




def test_per_convert():
    assert convert("3/4") == 75


def test_per_gauge():
    assert gauge(75) == '75%'  # Pass the percentage directly


def test_val_convert_invalid_numerator():
    with pytest.raises(ValueError):
        convert("4/3")  # Numerator greater than denominator


def test_val_convert_invalid_float():
    with pytest.raises(ValueError):
        convert("1.5/3")  # Invalid fraction format


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Test with zero as the denominator

def test_label_1_percent():
    assert gauge(1) == 'E'  # Test that 1% is labeled as 'E'

def test_label_99_percent():
    assert gauge(99) == 'F'  # Test that 99% is labeled as 'F'
