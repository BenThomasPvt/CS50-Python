import pytest
from um import count


def test_single_um():
    assert count("hello, um, world") == 1


def test_multiple_ums():
    assert count("um, um, um!") == 3


def test_no_um():
    assert count("yummy, happy, bumpy") == 0


def test_case_insensitivity():
    assert count("UM, um, Um") == 3


def test_um_as_substring():
    assert count("yummy, plumb, bumble") == 0


def test_um_at_boundaries():
    assert count("um!") == 1
    assert count("hello, um.") == 1
    assert count("um?") == 1
    assert count("um. um") == 2
