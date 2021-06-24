
import src.my_code


def test_double_it():
    assert 8 == src.my_code.double_it(4)
    assert 0 == src.my_code.double_it(0)
    assert -2 == src.my_code.double_it(-1)
