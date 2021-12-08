from cl import Check

import pytest


@pytest.fixture
def accum():
    return Check(1)


def test_initialize(accum):
    assert accum.number == 1


def test_add_one(accum):
    accum.add_to_me(1)
    assert accum.number == 2


def test_raise_error(accum):
    with pytest.raises(AttributeError, match='can\'t set attribute'):
        accum.number = 10
