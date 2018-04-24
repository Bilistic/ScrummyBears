import CtoF

def test_CtoF():
    val = 1
    if assert CtoF.CtoF(10) == 50:
        val = 0
    if assert CtoF.CtoF(11) == 55.8:
        val =  1
    return val
