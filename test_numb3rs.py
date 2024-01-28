from numb3rs import validate


def test_check_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3.4.5") == False

def test_check_number():
    assert validate(r"255.0.78.100") == True
    assert validate(r"275.2.3.4") == False
    assert validate(r"1.2555.1.1") == False
