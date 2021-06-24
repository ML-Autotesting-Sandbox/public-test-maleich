from my_code import double_it


def test_inc():
    assert 8 == double_it(4)
    assert 0 == double_it(0)
    assert -2 == double_it(-1)
