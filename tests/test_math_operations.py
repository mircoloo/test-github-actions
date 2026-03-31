from src.math_operations import add
import pytest


@pytest.mark.parametrize(("a", "b", "res"), [(1, 2, 3), (4, 5, 9)])
def test__add__correct(a: int, b: int, res: int):
    assert add(a, b) == res

@pytest.mark.parametrize(("a", "b", "res"), [(1, 2, 4)])

def test__add__wrong(a: int, b: int, res: int):
    assert not (add(a, b) == res)
