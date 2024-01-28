from numb3rs import validate


def test_check_format():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.4.5") == False

def test_check_number():
    assert validate("255.0.78.100") == True
    assert validate("275.2.3.4") == False
    assert validate("255.1342.2343.400") == False
