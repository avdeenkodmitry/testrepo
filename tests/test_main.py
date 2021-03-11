from main import function


def test_1():
    assert function(3, 6) is False


def test_2():
    assert function(10, 5) is True
