import pytest
from datetime import date
from seasons import calculate_age_in_minutes, minutes_to_words

# Test calculate_age_in_minutes function


def test_calculate_age_in_minutes_valid():
    # Let's assume the user was born on 2000-01-01
    birthdate = "2000-01-01"
    expected_minutes = (date.today() - date.fromisoformat(birthdate)).days * 24 * 60
    assert calculate_age_in_minutes(birthdate) == expected_minutes


def test_calculate_age_in_minutes_invalid_format():
    # Test if invalid date format raises an error
    with pytest.raises(SystemExit):
        calculate_age_in_minutes("01-01-2000")  # Invalid date format


def test_calculate_age_in_minutes_future_date():
    # Test if the birthdate is in the future
    future_date = (date.today().year + 1)  # Year ahead
    with pytest.raises(ValueError):  # It should raise ValueError or fail gracefully
        calculate_age_in_minutes(f"{future_date}-01-01")

# Test minutes_to_words function


def test_minutes_to_words_valid():
    minutes = 120  # 2 hours, 120 minutes
    assert minutes_to_words(minutes) == "One hundred twenty minutes"


def test_minutes_to_words_zero():
    minutes = 0
    assert minutes_to_words(minutes) == "Zero minutes"


def test_minutes_to_words_large_number():
    # Test a large number to ensure it's converted properly
    minutes = 1000000
    assert minutes_to_words(minutes) == "One million minutes"

# If you want to run the tests automatically using pytest:
# Run `pytest` in your terminal where this file is located.
