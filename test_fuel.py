from fuel import convert, gauge

def test_convert_gauge ():
    assert convert ("4/10") == 40
    assert gauge (99) == "F"
    assert gauge (1) == "E"
    assert gauge (25) == "25%"

