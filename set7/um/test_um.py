from um import count

def test_count():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("Um UM uM") == 3
    assert count("Umm") == 0
    assert count("Yummy") == 0