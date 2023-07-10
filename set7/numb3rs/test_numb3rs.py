from numb3rs import validate

def test_validate_fourdigits():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.256") == False

def test_validate_exceptions():
    assert validate("0.0.0.") == False
    assert validate("0.0") == False
    assert validate("255") == False
    assert validate("") == False
    assert validate("0.0.0.0.0") == False
