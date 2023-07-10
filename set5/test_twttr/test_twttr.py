from twttr import shorten

def test_shorten():
    assert shorten("hallo") == "hll"


def test_numeric():
    assert shorten("12345") == "12345"


def test_vowels():
    assert shorten("aeiou") == ""


def test_punctuation():
    assert shorten(".,!") == ".,!"


def test_capital():
    assert shorten("AEIOU") == ""