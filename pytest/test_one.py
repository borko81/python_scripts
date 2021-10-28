from typing import Type
from attr import Attribute
import pytest


def inx(x):
    return x + 1


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def check():
    raise ValueError("Some error")


def test_value_error_raise():
    with pytest.raises(ValueError) as er:
        check()
    assert "Some error" in str(er.value)


def test_full_comparning():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 != set2


def test_uppercae():
    assert "UPPER" == "upper".upper()


def capital_case(word):
    if not isinstance(word, str):
        raise TypeError("Provide string argument")
    return word.title()


def test_capital_case():
    assert capital_case("world") == "World"


def test_capital_case_raise_error():
    with pytest.raises(TypeError) as er:
        capital_case(10)
    assert "Provide string argument" == str(er.value)
