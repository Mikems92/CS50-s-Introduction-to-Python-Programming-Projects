from bank import value


def test_hello():
    assert value ("hello, world") == 0
    assert value ("Hello, world") == 0

def test_h():
    assert value ("how are you ?") == 20

def test_else():
    assert value ("What are you doing ?") == 100


