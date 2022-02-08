from collections import namedtuple
import pytest


def check(n):
    try:
        return n + "str"
    except TypeError:
        raise TypeError("Not valid")


def test_add():
    with pytest.raises(TypeError):
        check(10)



def test_ok():
    assert check("a") == "astr"
