from plates import is_valid

def test_is_valid_1():
    assert is_valid("c4") == False
    assert is_valid("CS") == True
    assert is_valid("gl") == True
    assert is_valid("44") == False

def test_is_valid_2():
    assert is_valid("HUIHUIY") == False
    assert is_valid("FUIFUI") == True
    assert is_valid("CS505") == True
    assert is_valid("AZERTYU") == False

def test_is_valid_3():
    assert is_valid("CS5A4B") == False
    assert is_valid("CSHB56") == True
    assert is_valid("GLRTY9") == True
    assert is_valid("BL34AE") == False

def test_is_valid_4():
    assert is_valid("CS0478") == False
    assert is_valid("QS0478") == False
    assert is_valid("FG,t;") == False
