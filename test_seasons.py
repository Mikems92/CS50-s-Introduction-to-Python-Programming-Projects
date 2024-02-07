import seasons


def test_check_format ():
    assert check_format ("2022-01-01") == True
    assert check_format ("January, 01 2022") == "Invalid date"

def test_convert ():
    assert convert ("2024-01-01") == "fifty-four thousand, seven hundred and twenty"
