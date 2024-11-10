import pytest
from seasons import Birthday


# Test correct dates
def test_Birthday_check_date():
    assert Birthday.check_date("1989-07-10") == True
    assert Birthday.check_date("2002-10-10") == True
    assert Birthday.check_date("2024-11-09") == True
