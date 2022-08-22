from main import sqr


def test_sqrfx_negNum():
    assert sqr(-2) == 4;
    assert sqr(-3) == 9;

def test_sqrfx_zero():
    assert sqr(0) == 0;

def test_sqrfx_posNum():
    assert sqr(2) == 4;
    assert sqr(3) == 9;

