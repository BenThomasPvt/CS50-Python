import pytest
from working import convert


def test_valid_times():
    # Test with different valid inputs
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_edge_cases():
    # Test edge cases like midnight and noon
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_invalid_times():
    # Test invalid times that should raise ValueError
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5")
