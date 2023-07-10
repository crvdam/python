from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("h") == 20

def test_numeric():
    assert value("123") == 100

def test_case():
    assert value("hElLo") == 0

def test_phrase():
    assert value("Hello I would like to pass this test") == 0


