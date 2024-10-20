import pytest
from twttr import shorten


# Test vowels lowercase
def test_l_u_case():

    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twiTteR") == "twTtR"

# Test numbers
def test_numbers():

    assert shorten("123") == "123"

# Test punctuation
def test_punctuation():
    assert shorten("!@#$%") == "!@#$%"