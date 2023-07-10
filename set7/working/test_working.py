from working import convert
import pytest

def test_value_error():
    with pytest.raises(ValueError):
        convert("1:00 AM 91:00 PM")
    with pytest.raises(ValueError):
        convert("1:99 to 1:00")
    with pytest.raises(ValueError):
        convert("1 AM 1 PM")
    with pytest.raises(ValueError):
        convert("01:00 AM - 99:00 PM")
    with pytest.raises(ValueError):
        convert("4 AM - 4 PM")
    with pytest.raises(ValueError):
        convert("12 AM1 PM")
    with pytest.raises(ValueError):
        convert("1:60 AM to 1:60 PM")

def test_hours_minutes():
    assert convert("1:00 AM to 1:45 PM") == "01:00 to 13:45"



