from fuel import convert, gauge
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_x_largerthan_y():
    with pytest.raises(ValueError):
        convert("2/1")

def test_wrong_integer():
    assert convert("1/5") > 0
    assert convert("1/5") <= 100
    with pytest.raises(ValueError):
        convert("111")
        convert("1/A")
        convert("A/1")
        convert("A/A")
        convert("1A/2")
        convert("1/2A")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(100) == "F"