from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAA") == True
    assert is_valid("AAAAAAA") == False

def test_start_alphabetical():
    assert is_valid("11AA") == False
    assert is_valid("AA11") == True
    assert is_valid("9!AA88") == False
    assert is_valid("1AAAA5") == False
    assert is_valid("9A") == False
    assert is_valid("99") == False

def test_no_middle_numeric():
    assert is_valid("AA11AA") == False
    assert is_valid("AAAA11") == True

def test_alpha_numeric():
    assert is_valid("AA,,AA") == False
    assert is_valid("AA111!") == False

def test_first_number_zero():
    assert is_valid("AAAA01") == False