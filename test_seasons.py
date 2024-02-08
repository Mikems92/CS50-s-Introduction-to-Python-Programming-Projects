from seasons import check_format, convert


def test_check_format ():
    assert check_format ("2022-01-01") == "2022-01-01"


