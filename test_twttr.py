from twttr import shorten

def test_shorten():
    assert shorten("bintou") == "bnt"
    assert shorten("fatiama00") == "ftm00"
    assert shorten("NOAH") == "NH"



