import pytest
import working


# Correct cases
def test_convert_correct():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert working.convert("5 PM to 9 AM") == "17:00 to 09:00"
    assert working.convert("9 AM to 05:00 PM") == "09:00 to 17:00"
    assert working.convert("09:00 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"


# Error test
def test_convert_error():
    with pytest.raises(ValueError):
        working.convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        working.convert("9 AM to 05:60 PM")
    with pytest.raises(ValueError):
        working.convert("09:60 AM to 05:00 PM")
    with pytest.raises(ValueError):
        working.convert("09:60 AM to 05:60 PM")
    with pytest.raises(ValueError):
        working.convert("cat to cat")
