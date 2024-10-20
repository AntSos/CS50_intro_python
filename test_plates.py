from plates import is_valid

# Test valid number of characters
def test_begining():

    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("5A") == False
    assert is_valid("58ANB") == False


# Test numbers at the begining
def test_lenght():

    assert is_valid("ANBNH02") == False
    assert is_valid("ANB58563") == False
    assert is_valid("CS") == True
    assert is_valid("ANBNUIO") == False
    assert is_valid("QWERTYYES") == False
    assert is_valid("ANERTYW") == False

# Test number 0 in the middle
def test_invalid_m_numbers():

    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("ANB02") == False
    assert is_valid("ANG06") == False
    assert is_valid("AN1BG") == False
    assert is_valid("BN6BG") == False

def test_symbols():
    assert is_valid("AN.>") == False
    assert is_valid("!@.>") == False
    assert is_valid("><AZ^") == False

