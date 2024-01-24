from bank import value


def test_hello():
    assert value ("hello, world") == f"${0}"

def test_h():
    assert value ("how are you ?") == f"${20}"

def test_else():
    assert value ("What are you doing ?") == f"${100}"


