def test_value_false():
    assert False


def test_value_true():
    assert True
    # pass


def test_value_empty_list():
    assert []


def test_value_full_list():
    assert [1, 2, 3]


def test_value_not_full_list():
    assert not [1, 2, 3]


def sum(n1, n2):
    return n1 + n2


def test_suma():
    assert sum(1, 1) == 2


def test_integradora():
    assert sum(1, 1) * sum(3, 4) == 14
